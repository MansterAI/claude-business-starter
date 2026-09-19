---
name: kpi-tracker
description: Use when a 10K Digital member wants to push their KPIs to their 10K Journey Tracker dashboard. Two modes — conversational (tu donnes tes chiffres, zéro setup, via le MCP) or auto-sync (avancé : Meta Ads + GoHighLevel). Triggers on "remplis mon KPI tracker", "envoie mes stats", "sync mes chiffres 10K", "update mon pilotage".
---

# KPI Tracker — envoyer tes chiffres dans ton tableau de bord 10K

> **Connexion 10K.** Cette skill envoie les chiffres dans le compte 10K : elle a besoin que le 10K soit branché. Sinon, propose de brancher en un clic (`/mcp` → `10k-digital`), gentiment.

## Ce que ça fait

Tu donnes tes chiffres de funnel → Claude les enregistre dans ton onglet **KPI** de l'app (une ligne par date × type de campagne, en *upsert* : rejouer ne crée pas de doublon, ça met à jour). **Aucune clé, aucun fichier à éditer** : ça passe par l'outil MCP `log_kpi_entry`, via ta connexion `/mcp` déjà active.

## Deux modes

- **Conversationnel (défaut, zéro setup)** — tu donnes tes chiffres, Claude les logue. Rien à installer, pas de Meta. C'est le mode normal.
- **Auto-sync (avancé)** — Claude tire les chiffres de Meta Ads + GoHighLevel tout seul. Nécessite des clés dans `.env`. Réservé aux avancés, pas nécessaire pour débuter.

## Les 3 types de campagne
`follow` (trafic profil / croissance), `dm` (messagerie), `lead_gen` (formulaires / leads).

## Champs `log_kpi_entry` (mets 0 ou omets ce que tu n'as pas)
Requis : `entry_date` (YYYY-MM-DD), `campaign_type`. Optionnels : `ad_spend`, `profile_visits`, `followers`, `qualified_followers`, `dms_sent`, `conversations`, `leads`, `qualified_leads`, `booked_calls`, `show_up_calls`, `closed_calls`, `cash_collected`, `revenue`, `notes`.

---

## Mode conversationnel (défaut, zéro setup)

Le plus simple : tu demandes ses chiffres, tu les enregistres via `log_kpi_entry`.

1. **Période.** « Pour quelle date ? (défaut : aujourd'hui) ». Une entrée = une journée. Répète pour rattraper plusieurs jours.
2. **Canaux actifs.** « Tu tournes quelles campagnes ? Follow, DM, Lead Gen ? » — ne demande que ceux qu'il utilise.
3. **Chiffres du funnel, par canal** (saute ce qui ne s'applique pas) :
   - **Follow** : Ad Spend, Profile Visits, Followers, Qualified Followers, Conversations, Booked Calls, Show Up, Closed, Cash Collected, Revenue.
   - **DM** : Ad Spend, DMs envoyés, Qualified Followers, Conversations, Booked Calls, Show Up, Closed, Cash Collected, Revenue.
   - **Lead Gen** : Ad Spend, Leads, Qualified Leads, Conversations, Booked Calls, Show Up, Closed, Cash Collected, Revenue.

   Rassure : « Mets 0 si tu ne l'as pas, on corrigera plus tard. »
4. **Récap + confirme** avant d'envoyer (Date · Type · Ad Spend · … · Revenue — « Je peux envoyer ? »).
5. **Enregistre** : appelle l'outil MCP **`log_kpi_entry`** une fois par (date × type) non vide (`notes: "conversationnel"`). N'envoie pas de ligne toute à 0.
6. **Confirme** (voir plus bas).

---

## Mode auto-sync (avancé : Meta Ads + GoHighLevel)

> Réservé au membre qui a mis ses clés dans `.env` (`META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID`, `GHL_API_KEY`, `GHL_LOCATION_ID`). Pas nécessaire pour débuter. Traite J-1 par défaut (fuseau America/Toronto), ou la plage demandée. À la fin, enregistre via `log_kpi_entry` comme le mode conversationnel.

### Meta Ads (par campagne, par jour)
```
GET https://graph.facebook.com/v21.0/{META_AD_ACCOUNT_ID}/insights
  ?level=campaign&time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}&time_increment=1
  &fields=campaign_id,campaign_name,spend,impressions,actions,inline_link_clicks
  &access_token={META_ACCESS_TOKEN}
```
Mappe chaque campagne vers un `campaign_type` d'après son nom (insensible à la casse) : contient `lead`/`formulaire` → `lead_gen` ; `dm`/`messenger`/`direct` → `dm` ; sinon → `follow`. Extrais : `ad_spend` = `spend` ; `leads` = actions `lead`/`onsite_conversion.lead_grouped` ; `profile_visits` = actions `profile_visit` ; `dms_sent` = actions `onsite_conversion.messaging_conversation_started_7d`. Agrège par type.

### GoHighLevel (convos + pipeline, par jour)
```
GET https://services.leadconnectorhq.com/conversations/search
  ?locationId={GHL_LOCATION_ID}&startAfterDate={epochMs}&endBeforeDate={epochMs}&limit=100
Headers: Authorization: Bearer {GHL_API_KEY} · Version: 2021-04-15 · Accept: application/json
```
Classe par date du dernier message inbound : `conversations` (≥1 échange bidirectionnel) ; `dms_sent` (≥1 message envoyé) ; `qualified_followers`/`qualified_leads` (≥3 échanges OU tag `qualified`/`hot`/`sql`) ; `booked_calls` (appointment créé, endpoint `/calendars/events`) ; `show_up_calls` (status `showed`) ; `closed_calls` (opportunity `won`) ; `cash_collected`/`revenue` (somme `monetaryValue` won/payées). Donnée absente → 0 + note dans `notes`, n'invente jamais.

Puis récap + `log_kpi_entry` par (date × type) avec `notes: "auto-sync meta+ghl"`.

---

## Confirmer

Montre un tableau récap (date · type · spend · conversations · booked · closed · cash · revenue) et dis :

> « C'est envoyé. Va voir dans l'app → onglet **KPI**. ⚠️ L'onglet ouvre sur le mois courant : si tu as loggé un autre mois, change le sélecteur de mois (ou clique **Année**) pour voir tes chiffres. »

## Règles

- **Toujours upsert** (la clé unique `(date, type)` rend le rejeu sûr).
- **N'écrase pas une saisie manuelle** sans demander : si une entrée existe déjà pour cette date/type avec des `notes` sans `conversationnel`/`auto-sync`, préviens avant.
- Montants en **CAD**. Ne jamais inventer un chiffre manquant → 0 + note.
