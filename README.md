# Claude Business Starter

Un template prêt à l'emploi pour organiser le contexte de ton entreprise dans Claude Code.

> **Principe :** Plus Claude connaît ton entreprise, plus il devient utile. Ce template te donne la structure pour alimenter Claude au fil du temps.

---

## Démarrage rapide

Tu n'as rien à remplir à la main. Trois étapes, et la première chose que Claude te demande, c'est de connecter ton compte Pilora.

### Étape 1 : Ouvre le dossier dans Claude
1. **Télécharge le ZIP** (ton lien de bonus) et **décompresse-le**.
2. Ouvre l'app **Claude** (desktop) → **Cowork / Code** → **ouvre le dossier** que tu viens de décompresser.

Pas de terminal, pas de git. *(Avancé : tu peux aussi faire `git clone https://github.com/MansterAI/claude-business-starter` et l'ouvrir dans Claude Code en ligne de commande. Tu utilises Codex ? Voir « Utiliser avec Codex » plus bas.)*

### Étape 2 : Connecte Pilora
Écris « on commence ». Claude te demande de brancher ton compte Pilora avant toute chose. Tape
```
/mcp
```
choisis **pilora** et connecte-toi avec ton compte. Le serveur est déjà configuré, tu n'as rien à installer. Si tu n'as pas encore de compte Pilora, crée-le d'abord sur [pilora.ai](https://www.pilora.ai) (c'est gratuit).

Cette connexion permet à Claude de lire ton tableau de bord d'entreprise (ta Fondation, tes stats, ton funnel) et de sauvegarder tout ce que vous faites ensemble.

### Étape 3 : Claude complète ta Fondation avec toi
Une fois branché, Claude te montre ce que Pilora contient déjà, puis te pose des questions seulement sur ce qui manque (histoire, brand, client idéal, offre, marché). Tu réponds, il rédige, tu valides, et c'est enregistré dans Pilora. Il termine en te préparant du contenu prêt à publier.

**North Star par défaut : générer du revenu rapidement.** Tout est orienté vers ça.

---

## Utiliser avec Codex

Le même dossier fonctionne avec Codex (OpenAI). Ouvre-le dans Codex, accepte de faire confiance au projet, puis connecte Pilora depuis ton terminal :
```bash
codex mcp login pilora
```
Écris ensuite « on commence ». Les skills se lancent avec `$` au lieu de `/` (par exemple `$demarrer`), ou en passant par `/skills`.

---

## Accès & abonnement

L'accès passe par ton compte Pilora. **L'usage est gratuit** pour l'essentiel : ton contexte, ton contenu, tes scripts de vente, tes KPI, ton suivi. Les **features qui font tourner de l'IA** demandent un abonnement : le **roleplay de vente**, et **Man AI** au-delà de **20 messages** d'essai.

---

## Légende des fichiers

| Symbole | Signification |
|---------|---------------|
| 🔴 | À remplir selon ton entreprise |
| ✅ | Déjà prêt à l'emploi |
| 📋 | Template avec sections guidées |

---

## Skills disponibles

### `/demarrer` *(à faire en premier)*
Lance l'onboarding : connecte Pilora en premier, importe ton contexte (histoire, brand, ICP, offre), définit ton style, et configure `CLAUDE.md` et tes fichiers.

### `/contenu`
Génère **hooks + un post prêt à publier** à partir de ta Fondation, ciblé sur ton client idéal et dans ton style. De quoi poster aujourd'hui.

### `/montage-video`
Monte un reel / short orienté rétention : script (hook → corps → CTA), sous-titres incrustés, coupe des silences, export vertical 9:16. Dans ton style, sans charte imposée.

### `/init-client`
Crée automatiquement une fiche client complète.
Claude pose 5 questions → génère le fichier dans `docs/clients/`.

### `/weekly-review`
Génère ta revue hebdomadaire business.
Claude analyse tes métriques + tâches en cours → rapport structuré + top 3 priorités.

### `/business-audit`
Audit complet de ton entreprise.
Claude lit tous tes fichiers de contexte → identifie les gaps + opportunités + 3 actions prioritaires.

### `/debloquer` *(clients DFY 4k)*
Installe le **bundle de skills premium** (créatives, gestion d'ads, analyse concurrents…) si tu es client du programme 4k. La vérification passe par ton compte Pilora.

### `/kpi-tracker`
Envoie tes chiffres de funnel dans ton onglet **KPI** de Pilora.
Deux modes : **conversationnel** (Claude te demande tes chiffres) ou **auto-sync** (Claude tire tes stats de Meta Ads + GoHighLevel).
Aucun setup : ça passe par ta connexion Pilora (voir « Envoyer tes chiffres dans Pilora » plus bas).

---

## Envoyer tes chiffres dans Pilora

Une fois Pilora connecté (étape 2), tu n'as rien d'autre à configurer. Tape :
```
/kpi-tracker
```
Claude te demande tes chiffres de la semaine et les envoie dans ton onglet **KPI**.

**Optionnel : auto-sync.** Si tu veux que Claude tire tes stats tout seul depuis **Meta Ads** et **GoHighLevel**, copie `.env.example` en `.env`, remplis les variables Meta/GHL, puis demande « sync auto ». Le `.env` n'est jamais poussé sur GitHub.

> ⚠️ Après l'envoi, va dans [Pilora](https://www.pilora.ai) → onglet KPI. L'onglet ouvre sur le **mois courant** : si tu as loggé un autre mois, change le sélecteur de mois (ou clique **Année**) pour voir tes chiffres.

---

## Exemples de prompts

Une fois tes fichiers remplis, voici ce que tu peux demander à Claude :

**Marketing**
> "Écris 3 hooks Instagram pour promouvoir mon offre [Offre 1] en ciblant [Avatar 1]"

**Ventes**
> "J'ai un appel avec un prospect qui hésite à cause du prix. Prépare-moi une réponse à l'objection 'c'est trop cher' pour notre offre [Offre 1]"

**Opérations**
> "Crée-moi une SOP pour [processus à documenter]"

**Stratégie**
> "Analyse mes métriques de la semaine et dis-moi sur quoi me concentrer la semaine prochaine"

**Clients**
> "Rédige un email de suivi pour [nom du client] qui n'a pas répondu depuis 2 semaines"

---

## Structure du projet

```
claude-business-starter/
├── CLAUDE.md              ← ✅ Rempli automatiquement par /demarrer
├── AGENTS.md              ← ✅ Point d'entrée pour Codex (renvoie à CLAUDE.md)
├── .mcp.json              ← ✅ Connexion Pilora pour Claude (via /mcp)
├── .codex/config.toml     ← ✅ Connexion Pilora pour Codex
├── .agents/skills/        ← ✅ Skills exposées à Codex (renvoient à .claude/skills/)
├── .env.example           ← 📋 Copier en .env (optionnel : auto-sync Meta/GHL)
├── .claude/
│   └── skills/            ← Skills Claude Code (/demarrer, /kpi-tracker, /montage-video...)
├── ai/
│   ├── context/           ← Ce que Claude sait de ton entreprise
│   ├── agents/            ← Spécialistes par département
│   ├── memory/            ← Mémoire de session en session
│   └── prompts/           ← ✅ Prompts réutilisables
└── docs/
    ├── brand/             ← 🔴 Identité visuelle et verbale
    ├── clients/           ← Fiches clients (générées avec /init-client)
    ├── marketing/         ← 🔴 Stratégie marketing
    ├── sales/             ← 🔴 Pipeline + ✅ objections universelles
    ├── fulfillment/       ← 🔴 SOPs et livraison
    └── finance/           ← 🔴 Métriques et objectifs
```

---

## Questions ?

Ce template est conçu pour évoluer avec ton entreprise. Tu peux :
- Ajouter de nouveaux fichiers clients dans `docs/clients/`
- Créer de nouvelles SOPs dans `docs/fulfillment/sop/`
- Enrichir les prompts dans `ai/prompts/` au fil de tes découvertes
- Ajouter tes propres skills dans `.claude/skills/`
