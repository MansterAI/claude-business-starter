# Claude Business Starter

Un template prêt à l'emploi pour organiser le contexte de ton entreprise dans Claude Code.

> **Principe :** Plus Claude connaît ton entreprise, plus il devient utile. Ce template te donne la structure pour alimenter Claude au fil du temps.

---

## Démarrage rapide

Tu n'as **rien à remplir à la main**. Tu télécharges le repo, tu ouvres Claude Code, et Claude t'accompagne dans une conversation d'installation.

### Étape 1 — Récupérer le repo
```bash
git clone https://github.com/MansterAI/claude-business-starter mon-entreprise
cd mon-entreprise
```
*(Ou télécharge le ZIP depuis GitHub et décompresse-le.)* Ouvre ensuite le dossier dans **Claude Code**.

### Étape 2 — Connecter ton tableau de bord 10K
Dans Claude Code, tape :
```
/mcp
```
Choisis **10k-digital** et connecte-toi avec ton compte 10K Digital. *(Le serveur est déjà pré-configuré dans le repo.)*

> ⚠️ **Avant** : va dans l'app 10K et complète les modules du début (ton **histoire**, ta **brand**, ton **ICP**, ton **offre**). Ces infos seront importées automatiquement dans ton Claude Code.

### Étape 3 — Commencer à chatter
Écris simplement à Claude (ex. « on commence ») ou tape :
```
/demarrer
```
Claude lance l'**onboarding** : il importe ton contexte depuis l'app 10K, te pose les questions manquantes, définit ton style d'écriture, et remplit `CLAUDE.md` + tes fichiers de contexte pour toi.

**North Star par défaut du système : générer du revenu rapidement.** Tout est orienté vers ça.

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
Lance l'onboarding : connecte le MCP 10K, importe ton contexte (histoire, brand, ICP, offre), définit ton style, et configure `CLAUDE.md` + tes fichiers.

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

### `/kpi-tracker` *(membres 10K Digital)*
Envoie tes chiffres de funnel dans ton onglet **KPI** de l'app 10K.
Deux modes : **conversationnel** (Claude te demande tes chiffres) ou **auto-sync** (Claude tire tes stats de Meta Ads + GoHighLevel).
Setup en 2 min → voir la section « Connecter ton tableau de bord 10K » plus bas.

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

## Connecter ton tableau de bord 10K *(membres 10K Digital)*

> **Deux connexions, deux usages :**
> - **`/mcp` (fait à l'étape 2)** → connexion générale : import de ton contexte business, skills, progression. C'est la principale.
> - **Clé `.env` ci-dessous** → sert **uniquement** à la skill `/kpi-tracker` pour logguer le détail de ton funnel. Optionnelle, à faire seulement si tu utilises `/kpi-tracker`.

La skill `/kpi-tracker` pousse tes chiffres dans l'onglet **KPI** de l'app 10K, automatiquement. Setup une seule fois :

**1. Génère ta clé API.** Dans l'app 10K → menu → **API Keys** (page `/api-keys`) → crée une clé (format `10k_...`).

**2. Crée ton `.env`.** Copie le modèle :
```bash
cp .env.example .env
```
Ouvre `.env` et colle ta clé dans `KPI_INGEST_KEY`. *(Le `.env` n'est jamais poussé sur GitHub — il est protégé par `.gitignore`.)*

**3. Utilise-la.** Dans Claude Code, tape :
```
/kpi-tracker
```
Claude te demande tes chiffres de la semaine et les envoie dans ton pilotage. C'est tout.

**Optionnel — auto-sync.** Si tu veux que Claude tire tes stats tout seul depuis **Meta Ads** et **GoHighLevel**, remplis aussi les variables Meta/GHL dans `.env` (voir `.env.example`), puis demande « sync auto ».

> ⚠️ Après l'envoi, va dans l'app → onglet KPI. L'onglet ouvre sur le **mois courant** : si tu as loggé un autre mois, change le sélecteur de mois (ou clique **Année**) pour voir tes chiffres.

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
├── .mcp.json              ← ✅ MCP 10K pré-configuré (connexion via /mcp)
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
- Ajouter tes propres skills dans `skills/`
