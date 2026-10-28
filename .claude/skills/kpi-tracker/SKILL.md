---
name: kpi-tracker
description: Use when a member wants to push their KPIs to their Pilora dashboard. Two modes: conversational (tu donnes tes chiffres, zéro setup, via le MCP) or auto-sync (avancé : Meta Ads + GoHighLevel). Triggers on "remplis mon KPI tracker", "envoie mes stats", "sync mes chiffres Pilora", "update mon pilotage".
---

# KPI Tracker : envoyer tes chiffres dans ton tableau de bord Pilora

> **Connexion Pilora.** Cette skill envoie les chiffres dans le compte Pilora du membre : elle a besoin que Pilora soit branché. Sinon, fais-le connecter d'abord (dans Claude, `/mcp` → `pilora` ; dans Codex, `codex mcp login pilora` au terminal), gentiment.

## Ce que ça fait

Le membre donne ses chiffres, tu les enregistres dans son onglet **KPI** de Pilora avec l'outil MCP **`log_kpi_entry`** : une ligne par **date × source**. Rejouer met à jour la ligne au lieu d'en créer une autre. Aucune clé, aucun fichier à éditer.

## Les deux règles à ne jamais casser

1. **Une personne = une source.** Chaque personne va dans la source par laquelle elle est arrivée (son premier contact), puis avance dans le funnel. Elle n'est jamais comptée deux fois. Quelqu'un qui follow puis écrit en DM reste dans **Follow**.
2. **Chaque étape est un sous-groupe de la précédente.** Contacts ≥ Qualifiés ≥ Conversations ≥ Appels bookés ≥ Présents ≥ Closes après appel. Le contrôle se fait sur les **totaux du mois** : une journée isolée peut dépasser (quelqu'un a follow le 3 et converse le 10), le mois non.

## Les 5 sources (`campaign_type`)

| Source | `campaign_type` | Contacts = | Étapes avant les contacts (pas des personnes) |
|---|---|---|---|
| Follow (pub profil) | `follow` | `followers` : nouveaux follows | `ad_spend`, `profile_visits` |
| DM (pub DM) | `dm` | `dms_sent` : DMs reçus de la pub | `ad_spend` |
| Inbound (organique) | `inbound` | `dms_sent` : DMs entrants spontanés (contenu, bouche-à-oreille) | aucune |
| Lead Gen | `lead_gen` | `leads` : formulaires remplis | `ad_spend` |
| Webinaire | `webinar` | `webinar_attendees` : présents au webinaire | `ad_spend`, puis `webinar_registrations` (inscrits, ≥ présents) |

En cas de doute entre DM et Inbound : si la personne a écrit en réponse à une pub DM, c'est `dm`. Sinon (elle a vu un contenu, on lui a parlé de toi), c'est `inbound`.

## Le funnel, étape par étape (identique pour les 5 sources)

| # | Étape | Champ | Ce qu'on compte, exactement |
|---|---|---|---|
| 1 | Contacts | voir tableau des sources | Les gens arrivés par cette source |
| 2 | Qualifiés | `qualified_contacts` | Parmi les contacts, ceux qui sont dans la cible (business en ligne confirmée, selon l'ICP du membre) |
| 3 | Conversations | `conversations` | Parmi les qualifiés, ceux avec qui une discussion de vente a vraiment commencé : questions objectifs/problèmes posées **et** réponse reçue |
| 4 | Appels bookés | `booked_calls` | Parmi les conversations, ceux qui ont un appel de vente au calendrier |
| 5 | Présents | `show_up_calls` | Parmi les bookés, ceux qui se sont présentés à l'appel |
| 6a | Closes après appel | `closed_calls` | Ventes conclues après un appel (≤ Présents) |
| 6b | Ventes sans appel | `direct_sales` | Ventes conclues sans appel (lien de paiement en DM, achat pendant le webinaire), parmi les conversations |
| | Cash encaissé | `cash_collected` | L'argent reçu **ce jour-là** (un versement mensuel compte le jour où il arrive) |
| | Revenu | `revenue` | La valeur du contrat, comptée **une seule fois**, le jour du close (0 pour un versement mensuel) |

Closes au total = `closed_calls` + `direct_sales`. Taux de closing = `closed_calls` ÷ `show_up_calls`.

**Ne plus utiliser** : `qualified_followers`, `qualified_leads`, `dms_qualified` (anciens champs). Utilise `qualified_contacts`.

Tous les champs sont optionnels sauf `entry_date` (YYYY-MM-DD) et `campaign_type`. Ce que le membre n'a pas : omets-le, n'invente jamais.

---

## Quick log (express, rituel hebdo)

Pour une relance rapide, demande l'essentiel dans l'ordre du funnel, sur la **source principale** du membre (demande-la s'il ne l'a jamais dite) :

1. Combien de **nouveaux contacts** ? (follows, DMs, formulaires… selon la source)
2. Combien de **conversations de vente** ? (questions posées et réponse reçue)
3. Combien d'**appels bookés**, et combien se sont **présentés** ?
4. Combien de **ventes**, dont combien **sans appel** ?
5. Combien de **cash** encaissé, et pour les nouvelles ventes, la **valeur du contrat** ?

S'il ne connaît pas le nombre de qualifiés, mets `qualified_contacts` = `conversations` : une personne en conversation de vente a été jugée dans la cible. Vérifie le funnel (voir plus bas), récapitule, puis enregistre. Propose ensuite de compléter le funnel complet s'il en a envie.

## Mode conversationnel (défaut, zéro setup)

1. **Période.** « Pour quelle date ? (défaut : aujourd'hui) » Une entrée = une journée. Pour une semaine, une ligne par jour, ou une seule ligne datée du dernier jour s'il n'a que des totaux.
2. **Sources.** « D'où viennent tes prospects ? Follow, DM pub, Inbound, Lead Gen, Webinaire ? » Ne demande que celles qu'il utilise. Rappelle la règle : une personne = la source par laquelle elle est arrivée.
3. **Chiffres, source par source, dans l'ordre du funnel** : étapes avant les contacts (dépense pub, visites, inscrits), puis Contacts → Qualifiés → Conversations → Appels bookés → Présents → Closes après appel / Ventes sans appel → Cash → Revenu. Explique chaque étape avec la définition du tableau quand il hésite.
4. **Vérifie le funnel** avant d'envoyer (voir plus bas).
5. **Récap + confirmation** : un tableau Date · Source · Contacts · Qualifiés · Conversations · Bookés · Présents · Closes (dont sans appel) · Cash · Revenu, puis « Je peux envoyer ? ».
6. **Enregistre** : `log_kpi_entry` une fois par (date × source) qui a au moins un chiffre, avec `notes: "conversationnel"`. N'envoie pas de ligne toute à 0.
7. **Confirme** (voir plus bas).

## Vérifier le funnel avant d'envoyer

Sur le total de la période, pour chaque source, chaque étape doit être ≤ la précédente. Si ce n'est pas le cas, ne corrige pas tout seul : montre l'écart et pose la question.

> « Tu as 4 conversations mais 2 qualifiés. Une conversation de vente se fait avec quelqu'un dans ta cible : est-ce qu'il y avait en fait 4 qualifiés, ou 2 conversations ? »

Erreurs fréquentes à repérer :
- Compter comme « conversation » toute personne qui a répondu, même hors cible. Une conversation = questions objectifs/problèmes posées et réponse reçue, chez un qualifié.
- Compter dans DM quelqu'un qui était arrivé par un follow (il reste dans Follow).
- Mettre le montant total d'un contrat payé en plusieurs fois dans le cash du jour du close. Cash = ce qui est entré ce jour-là ; le total va dans Revenu.
- Compter un versement mensuel comme une nouvelle vente (c'est du cash, 0 close, 0 revenu).

Après l'envoi, `log_kpi_entry` renvoie une liste `warnings` si un total du mois dépasse l'étape précédente. Montre ces avertissements au membre et propose de corriger.

---

## Mode auto-sync (avancé : Meta Ads + GoHighLevel)

> Réservé au membre qui a mis ses clés dans `.env` (`META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID`, `GHL_API_KEY`, `GHL_LOCATION_ID`). Pas nécessaire pour débuter. Traite J-1 par défaut (fuseau America/Toronto), ou la plage demandée. Termine par la vérification du funnel et `log_kpi_entry`, comme le mode conversationnel.

### Meta Ads (étapes avant les contacts, par campagne et par jour)
```
GET https://graph.facebook.com/v21.0/{META_AD_ACCOUNT_ID}/insights
  ?level=campaign&time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}&time_increment=1
  &fields=campaign_id,campaign_name,spend,impressions,actions,inline_link_clicks
  &access_token={META_ACCESS_TOKEN}
```
Range chaque campagne dans une source d'après son nom (insensible à la casse) : `webinaire`/`webinar` → `webinar` ; `lead`/`formulaire` → `lead_gen` ; `dm`/`messenger`/`direct` → `dm` ; sinon → `follow`. Demande au membre si un nom est ambigu. Extrais : `ad_spend` = `spend` ; `profile_visits` = actions `profile_visit` (follow). Les contacts (follows, DMs, leads) se comptent dans GHL, pas dans Meta, pour suivre les mêmes personnes jusqu'au close.

### GoHighLevel (une personne, une source, puis son parcours)
```
GET https://services.leadconnectorhq.com/conversations/search
  ?locationId={GHL_LOCATION_ID}&startAfterDate={epochMs}&endBeforeDate={epochMs}&limit=100
Headers: Authorization: Bearer {GHL_API_KEY} · Version: 2021-04-15 · Accept: application/json
```
Pour chaque contact :
1. **Source** (premier contact) : 1er message = notre message automatique de bienvenue après un follow → `follow` ; il a écrit en premier un jour où une campagne DM dépensait → `dm`, sinon → `inbound` ; contact créé par un formulaire → `lead_gen` ; inscription au webinaire → `webinar`.
2. **Dates de chaque étape** : contact = 1er échange ; qualifié = 1er message qui confirme une business dans la cible (ou tag `qualified`/`icp`) ; conversation = questions objectifs/problèmes envoyées puis réponse reçue ; appel booké = rendez-vous créé (`/calendars/events`) ; présent = statut `showed` ; close = opportunité `won` (après appel si un rendez-vous `showed` existe, sinon vente sans appel).
3. **Compte chaque étape le jour où elle est atteinte**, dans la source de la personne. Si une personne a booké sans trace de conversation, compte-la quand même comme conversation et qualifiée (elle est forcément passée par là).
4. `cash_collected` = paiements reçus ce jour-là ; `revenue` = `monetaryValue` de l'opportunité le jour du close.

Donnée absente → omets-la et ajoute une note dans `notes`, n'invente jamais. Puis vérification du funnel, récap et `log_kpi_entry` par (date × source) avec `notes: "auto-sync meta+ghl"`.

---

## Confirmer

Montre le tableau récap et dis :

> « C'est envoyé. Va voir dans Pilora (https://www.pilora.ai) → onglet **KPI** : chaque source a son onglet, et l'Aperçu montre d'où viennent tes ventes. Une étape en rouge veut dire qu'elle dépasse la précédente sur le mois : on peut la corriger ensemble. »

## Règles

- **Rejouer est sûr** : la clé `(date, source)` met à jour la ligne existante, et seuls les champs envoyés changent.
- **N'écrase pas une saisie manuelle** sans demander : si une entrée existe déjà pour cette date et cette source avec des `notes` sans `conversationnel`/`auto-sync`, préviens avant.
- Montants en **CAD**. Un chiffre manquant n'est jamais inventé.
