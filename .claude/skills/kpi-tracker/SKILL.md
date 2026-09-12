---
name: kpi-tracker
description: Use when a 10K Digital member wants to push their KPIs to their 10K Journey Tracker dashboard. Two modes — conversational (asks you your numbers, zero external API) or auto-sync (pulls Meta Ads + GoHighLevel). Triggers on "remplis mon KPI tracker", "envoie mes stats", "sync mes chiffres 10K", "update mon pilotage".
---

# KPI Tracker — sync vers ton tableau de bord 10K

> **Réservé aux membres du programme 10K Digital.** Cette skill envoie tes chiffres de funnel dans ton onglet **KPI** de l'app (page `/kpis`). Chaque membre n'écrit que ses propres données — c'est ta clé API qui t'identifie.

## Ce que ça fait

Tu donnes tes chiffres (à la main, ou tirés de Meta/GHL) → la skill les envoie dans la table `campaign_entries` de ton compte, via l'endpoint sécurisé `campaign-ingest`. **Une ligne par (date, type de campagne)**, en *upsert* : rejouer la skill ne crée pas de doublon, ça met à jour.

## Prérequis (une seule fois)

1. Dans l'app 10K, va sur **API Keys** (page `/api-keys`) et **génère une clé** (format `10k_...`).
2. Copie `.env.example` en `.env` et colle ta clé dans `KPI_INGEST_KEY`.
3. (Optionnel, mode auto-sync) remplis aussi les variables Meta / GHL.

> Le `.env` est protégé par `.gitignore` — il ne partira jamais sur GitHub. Ne colle **jamais** une clé directement dans un fichier suivi par Git.

## L'endpoint (fixe, ne pas changer)

```
POST https://nmqxrjqznuanccgulcrc.supabase.co/functions/v1/campaign-ingest
Authorization: Bearer <KPI_INGEST_KEY>
Content-Type: application/json
Body: { "entries": [ { "entry_date": "YYYY-MM-DD", "campaign_type": "follow|dm|lead_gen", ... } ] }
```

Réponse succès : `{ "success": true, "entries_upserted": N }`.

Les 3 **types de campagne** valides : `follow` (trafic profil / croissance), `dm` (campagnes messagerie), `lead_gen` (formulaires / leads).

Champs numériques acceptés (mets 0 ou omets ceux que tu n'as pas) :
`ad_spend`, `profile_visits`, `followers`, `qualified_followers`, `dms_sent`, `dms_qualified`, `leads`, `qualified_leads`, `conversations`, `booked_calls`, `show_up_calls`, `closed_calls`, `cash_collected`, `revenue`. Plus `notes` (texte libre).

---

## Étape 0 — Charger la clé

Lis le fichier `.env` à la racine et récupère `KPI_INGEST_KEY`.
- **Absente ou vide ?** Arrête-toi et dis au membre : « Génère ta clé dans l'app (page /api-keys) et colle-la dans `.env` sous `KPI_INGEST_KEY`, puis relance-moi. »

Décide ensuite du mode :
- Si `META_ACCESS_TOKEN` **et** `GHL_API_KEY` sont remplis **et** que le membre demande explicitement un « sync auto » → **Mode auto-sync** (étape B).
- Sinon → **Mode conversationnel** (étape A). C'est le défaut.

---

## Étape A — Mode conversationnel (défaut, zéro API externe)

Le plus simple : tu demandes ses chiffres, tu les envoies.

1. **Demande la période.** « Pour quelle date veux-tu logger ? (défaut : aujourd'hui) ». Une entrée = une journée. Pour rattraper plusieurs jours, répète.

2. **Demande les canaux actifs.** « Tu tournes quelles campagnes ? Follow (croissance profil), DM, Lead Gen ? » — ne demande que les canaux qu'il utilise.

3. **Pour chaque canal, demande les chiffres du funnel** (dans l'ordre, saute ce qui ne s'applique pas) :
   - **Follow** : Ad Spend, Profile Visits, Followers, Qualified Followers, Conversations, Booked Calls, Show Up, Closed, Cash Collected, Revenue.
   - **DM** : Ad Spend, DMs envoyés, DMs qualifiés, Conversations, Booked Calls, Show Up, Closed, Cash Collected, Revenue.
   - **Lead Gen** : Ad Spend, Leads, Conversations, Qualified Leads, Booked Calls, Show Up, Closed, Cash Collected, Revenue.

   Rassure : « Mets 0 si tu n'as pas le chiffre, on pourra corriger plus tard. »

4. **Montre le récap et fais confirmer** avant d'envoyer :
   > Date · Type · Ad Spend · … · Revenue — « Je peux envoyer ? »

5. **Envoie** (étape C).

---

## Étape B — Mode auto-sync (avancé : Meta Ads + GoHighLevel)

Pour le membre qui a connecté ses comptes. Traite J-1 par défaut (fuseau America/Toronto), ou la plage demandée.

### B1 — Meta Ads (par campagne, par jour)

```
GET https://graph.facebook.com/v21.0/{META_AD_ACCOUNT_ID}/insights
  ?level=campaign
  &time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}
  &time_increment=1
  &fields=campaign_id,campaign_name,spend,impressions,actions,inline_link_clicks
  &access_token={META_ACCESS_TOKEN}
```

Mappe chaque campagne vers un `campaign_type` d'après son nom (insensible à la casse) :
- contient `lead` ou `formulaire` → `lead_gen`
- contient `dm`, `messenger`, `direct` → `dm`
- sinon (croissance / awareness / followers / profil) → `follow`

Extrais : `ad_spend` = `spend` ; `leads` (lead_gen) = actions `lead`/`onsite_conversion.lead_grouped` ; `profile_visits` (follow) = actions contenant `profile_visit` ; `dms_sent` (dm) = actions `onsite_conversion.messaging_conversation_started_7d`. Agrège par type.

### B2 — GoHighLevel (convos + pipeline, par jour)

```
GET https://services.leadconnectorhq.com/conversations/search
  ?locationId={GHL_LOCATION_ID}&startAfterDate={epochMs}&endBeforeDate={epochMs}&limit=100
Headers: Authorization: Bearer {GHL_API_KEY} · Version: 2021-04-15 · Accept: application/json
```

Pour chaque convo FB/IG, classe par date du dernier message inbound :
- `conversations` : ≥1 échange bidirectionnel dans la journée.
- `dms_sent` : convos où le membre a envoyé ≥1 message ce jour.
- `dms_qualified` / `qualified_followers` : ≥3 échanges OU tag GHL `qualified`/`hot`/`sql`.
- `booked_calls` : appointment GHL créé ce jour (endpoint `/calendars/events`).
- `show_up_calls` : appointment status `showed` ; `closed_calls` : opportunity `won` ce jour.
- `cash_collected` / `revenue` : somme des `monetaryValue` d'opportunities won/payées ce jour.

Donnée absente → laisse 0 et **note-le dans `notes`**, n'invente jamais.

### B3 — Montre le récap au membre, puis envoie (étape C).

---

## Étape C — Envoyer (commun aux 2 modes)

Construis le payload (une entrée par date × type non vide — **n'envoie pas de ligne toute à 0**), ajoute `"notes"` (ex. `"conversationnel"` ou `"auto-sync meta+ghl"`), puis :

```bash
curl -s -w '\n[HTTP %{http_code}]\n' -X POST \
  "https://nmqxrjqznuanccgulcrc.supabase.co/functions/v1/campaign-ingest" \
  -H "Authorization: Bearer $KPI_INGEST_KEY" \
  -H "Content-Type: application/json" \
  -d '{"entries":[ ... ]}'
```

- **200 + `entries_upserted`** → succès.
- **401** → clé invalide/absente → renvoie le membre à `/api-keys`.
- **400** → un `entry_date` (format `YYYY-MM-DD`) ou un `campaign_type` est invalide → corrige et rejoue.

## Étape D — Confirmer

Montre au membre un tableau récap (date · type · spend · conversations · booked · closed · cash · revenue) et dis-lui :

> « C'est envoyé. Va voir dans l'app → onglet **KPI**. ⚠️ L'onglet ouvre sur le mois courant : si tu as loggé un autre mois, change le sélecteur de mois (ou clique l'onglet **Année**) pour voir tes chiffres. »

## Règles

- **Toujours upsert**, jamais d'insert pur (la clé unique `(user_id, entry_date, campaign_type)` rend le rejeu sûr).
- **N'écrase pas une saisie manuelle** sans demander : si une entrée existe déjà pour cette date/type avec des `notes` qui ne contiennent pas `conversationnel`/`auto-sync`, préviens avant.
- Montants en **CAD**. Ne jamais inventer un chiffre manquant → 0 + note.
- Ne mets jamais la clé API dans un fichier suivi par Git, ni dans un message. Elle vit uniquement dans `.env`.
