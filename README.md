# Claude Business Starter

Un template prêt à l'emploi pour organiser le contexte de ton entreprise dans Claude Code.

> **Principe :** Plus Claude connaît ton entreprise, plus il devient utile. Ce template te donne la structure pour alimenter Claude au fil du temps.

---

## Démarrage rapide

### Étape 0 — Cloner le repo
```bash
git clone https://github.com/[ton-username]/claude-business-starter mon-entreprise
cd mon-entreprise
code .  # Ouvrir dans VS Code avec Claude Code
```

### Étape 1 — Remplir `CLAUDE.md` *(15 min)*
C'est le fichier le plus important. Claude le lit avant chaque conversation.
Remplis les sections marquées `[REMPLIR]` avec les infos de ton entreprise.

### Étape 2 — Remplir `ai/context/business.md` *(20 min)*
Vision, offres, positionnement, différenciateur.

### Étape 3 — Remplir `ai/context/audience.md` *(20 min)*
Tes 3 types de clients idéaux, leurs douleurs, ce qui les déclenche.

### Étape 4 — Remplir `docs/brand/voice-tone.md` *(10 min)*
Comment tu parles, ce que tu dis, ce que tu évites.

### Étape 5 — Créer ta première fiche client *(5 min)*
Tape dans Claude Code : `/init-client`
Claude va te poser 5 questions et créer le fichier automatiquement.

### Étape 6 — Remplir les contextes agents *(10 min chacun)*
`ai/agents/marketing/context.md`, `sales/context.md`, `fulfillment/context.md`
Ces fichiers permettent à Claude de comprendre où tu en es dans chaque département.

---

## Légende des fichiers

| Symbole | Signification |
|---------|---------------|
| 🔴 | À remplir selon ton entreprise |
| ✅ | Déjà prêt à l'emploi |
| 📋 | Template avec sections guidées |

---

## Skills disponibles

### `/init-client`
Crée automatiquement une fiche client complète.
Claude pose 5 questions → génère le fichier dans `docs/clients/`.

### `/weekly-review`
Génère ta revue hebdomadaire business.
Claude analyse tes métriques + tâches en cours → rapport structuré + top 3 priorités.

### `/business-audit`
Audit complet de ton entreprise.
Claude lit tous tes fichiers de contexte → identifie les gaps + opportunités + 3 actions prioritaires.

---

## Skills recommandés à installer

Ces skills améliorent la façon dont Claude travaille avec toi :

```bash
# 1. Cloner le repo superpowers
git clone https://github.com/obra/superpowers.git ~/.claude/plugins/superpowers

# 2. Les skills sont maintenant disponibles dans Claude Code
```

Skills recommandés une fois installés :
- `superpowers:brainstorming` — avant chaque nouveau projet ou feature
- `superpowers:writing-plans` — pour planifier avant d'agir
- `superpowers:systematic-debugging` — pour résoudre des problèmes méthodiquement
- `superpowers:verification-before-completion` — pour valider avant de dire "c'est fait"

👉 Repo officiel : [github.com/obra/superpowers](https://github.com/obra/superpowers)

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
├── CLAUDE.md              ← 🔴 Remplir en premier
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
- Ajouter tes propres skills dans `skills/`
