# CLAUDE.md — [REMPLIR: Nom de ton entreprise]

<!-- 📋 TEMPLATE : remplir les sections marquées [REMPLIR] -->
<!-- Ce fichier est lu par Claude AVANT chaque conversation. C'est le cerveau de ton projet. -->

## Qui je suis

**Entreprise :** [REMPLIR: Nom de l'entreprise]
**Secteur :** [REMPLIR: ex. agence marketing, coaching, e-commerce, service local...]
**Fondateur :** [REMPLIR: Ton nom]
**Ville / Région :** [REMPLIR: ex. Montréal, Québec]

**North Star :** [REMPLIR: Ton objectif principal, ex. "100 000 $/mois d'ici décembre 2026"]

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

**Comment je parle :** [REMPLIR: ex. direct, chaleureux, expert, sans jargon...]

**Vocabulaire à UTILISER :** [REMPLIR: ex. "système", "résultats", "concret", "étape par étape"]

**Vocabulaire à ÉVITER :** [REMPLIR: ex. "synergies", "disruptif", "solution innovante", promesses vagues]

**Langue principale :** [REMPLIR: Français / Anglais / Bilingue]

---

## Routing — quoi lire selon la tâche

| Tâche | Fichier à lire |
|-------|----------------|
| Comprendre l'entreprise | `ai/context/business.md` |
| Comprendre les clients | `ai/context/audience.md` |
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
- **TOUJOURS** montrer ce qui va changer avant toute opération d'écriture
- [REMPLIR: ajouter tes propres règles si nécessaire]

---

## MCP & Outils disponibles

- [REMPLIR: ex. Notion, CRM (GoHighLevel, HubSpot...), Meta Ads, etc.]
- [REMPLIR: ou écrire "Aucun pour l'instant" si tu n'as pas encore configuré de MCP]

---

## Skills disponibles dans ce projet

| Commande | Description |
|----------|-------------|
| `/init-client` | Créer une nouvelle fiche client |
| `/weekly-review` | Générer la revue hebdomadaire |
| `/business-audit` | Audit complet de l'entreprise |
