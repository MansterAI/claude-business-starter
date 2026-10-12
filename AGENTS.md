# AGENTS.md

Ce fichier est lu par Codex. Les instructions du projet sont dans `CLAUDE.md` : lis-le en entier au début de chaque session et applique-le tel quel, même si son nom mentionne Claude. C'est lui que l'onboarding remplit avec les informations du membre.

## Ce qui change sous Codex

- **Connexion Pilora.** Le serveur `pilora` est déclaré dans `.codex/config.toml`. Le membre se connecte en tapant `codex mcp login pilora` dans son terminal (la commande `/mcp` de `CLAUDE.md` est celle de Claude Code). Si le serveur n'apparaît pas, le projet n'est probablement pas encore marqué comme « trusted » dans Codex.
- **Skills.** Elles sont exposées dans `.agents/skills/` et se lancent avec `$nom` (ex. `$demarrer`) ou par `/skills`. Chacune renvoie au fichier complet dans `.claude/skills/<nom>/SKILL.md`, qui reste la seule version à modifier.
- **Commandes.** Quand `CLAUDE.md` ou une skill écrit `/demarrer`, `/contenu` ou `/kpi-tracker`, lance la skill du même nom.

## Première conversation

Si `ai/context/business.md` contient encore des `[REMPLIR]`, lance la skill `demarrer`. La première étape est toujours la connexion à Pilora, avant toute question sur la business du membre.
