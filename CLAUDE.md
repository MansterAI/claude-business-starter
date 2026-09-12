# CLAUDE.md — [REMPLIR: Nom de ton entreprise]

<!-- Ce fichier est lu par Claude AVANT chaque conversation. C'est le cerveau de ton projet. -->
<!-- 📋 TEMPLATE : les sections [REMPLIR] se complètent automatiquement pendant l'onboarding. -->

## 🚀 PROTOCOLE D'ONBOARDING — à exécuter EN PRIORITÉ

**Si ce fichier contient encore des `[REMPLIR]` OU si `ai/context/business.md` n'est pas personnalisé** → le projet n'est pas encore configuré. AVANT de répondre à toute autre demande, lance l'onboarding avec le skill **`/demarrer`** :

1. Accueille le membre en français québécois.
2. Fais-lui **connecter le MCP 10K** (`/mcp` → `10k-digital` → login).
3. **Importe son contexte** de l'app via `get_my_context` (histoire, brand, ICP, offre, marché) → écris-le ici et dans `ai/context/`.
4. S'il manque des infos dans l'app → dis-lui d'aller **compléter les modules 10K**, puis réimporte.
5. Définis son **style d'écriture** → `docs/brand/voice-tone.md`.
6. Confirme le **North Star**.

Suis le détail du skill `/demarrer`. **Montre toujours** ce que tu vas écrire avant d'écrire.

---

## Qui je suis

**Entreprise :** [REMPLIR: Nom de l'entreprise]
**Secteur :** [REMPLIR: ex. agence marketing, coaching, e-commerce, service local...]
**Fondateur :** [REMPLIR: Ton nom]
**Ville / Région :** [REMPLIR: ex. Montréal, Québec]

**North Star :** Générer du revenu rapidement <!-- objectif par défaut — précise-le pendant l'onboarding, ex. "signer 3 clients d'ici 60 jours" -->

**Mission en une phrase :** [REMPLIR: Ce que tu fais et pour qui]

---

## Offres principales

### Offre 1 : [REMPLIR: Nom de l'offre]
- **Prix :** [REMPLIR]
- **Livraison :** [REMPLIR: ex. 4 semaines, mensuel, one-time]
- **Pour qui :** [REMPLIR: type de client idéal]
- **Résultat promis :** [REMPLIR]

### Offre 2 : [REMPLIR: Nom de l'offre] *(optionnel)*
- **Prix :** [REMPLIR]
- **Livraison :** [REMPLIR]
- **Pour qui :** [REMPLIR]

---

## Voix & Ton

> Détail complet dans `docs/brand/voice-tone.md` (rempli à l'onboarding). Relis-le AVANT tout texte destiné à un humain.

**Comment je parle :** [REMPLIR]
**Vocabulaire à UTILISER :** [REMPLIR]
**Vocabulaire à ÉVITER :** [REMPLIR]
**Langue principale :** [REMPLIR: Français / Anglais / Bilingue]

---

## Routing — quoi lire selon la tâche

| Tâche | Fichier à lire |
|-------|----------------|
| Comprendre l'entreprise | `ai/context/business.md` |
| Comprendre les clients | `ai/context/audience.md` |
| Style d'écriture (avant tout texte humain) | `docs/brand/voice-tone.md` |
| Tâches marketing / contenu | `ai/agents/marketing/` |
| Tâches ventes / pipeline | `ai/agents/sales/` |
| Livraison / opérations | `ai/agents/fulfillment/` |
| Continuité de session | `ai/memory/in-progress.md` |
| Décisions passées | `ai/memory/decisions.md` |
| Fiche client spécifique | `docs/clients/[nom-client].md` |

---

## Règles absolues

- **JAMAIS** envoyer un email ou message au nom de l'entreprise sans confirmation explicite
- **JAMAIS** modifier des budgets publicitaires sans confirmation
- **JAMAIS** supprimer des fichiers sans confirmation
- **JAMAIS** publier une vidéo ou un post à ta place sans feu vert explicite
- **TOUJOURS** montrer ce qui va changer avant toute opération d'écriture
- [REMPLIR: ajouter tes propres règles pendant l'onboarding]

---

## MCP & Outils disponibles

- **10k-digital** (pré-configuré dans `.mcp.json`) — ton tableau de bord 10K : contexte business (`get_my_context` / `set_my_context`), KPIs (`log_kpi_entry`), progression, pipeline de contenu, scripts de vente. **Connexion : `/mcp` → `10k-digital` → login avec ton compte 10K.**
- [REMPLIR: autres outils que tu ajoutes — Notion, CRM, Meta Ads... ou "aucun pour l'instant"]

---

## Skills disponibles dans ce projet

| Commande | Description |
|----------|-------------|
| `/demarrer` | **Onboarding** — configure ton projet et importe ton contexte 10K (à faire en premier) |
| `/init-client` | Créer une nouvelle fiche client |
| `/kpi-tracker` | Envoyer tes chiffres de funnel dans ton tableau de bord 10K |
| `/montage-video` | Monter un reel / short orienté rétention (script → sous-titres → export) |
| `/weekly-review` | Générer la revue hebdomadaire |
| `/business-audit` | Audit complet de l'entreprise |
