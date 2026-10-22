# Claude Business Starter

Un template prêt à l'emploi pour organiser le contexte de ton entreprise dans Claude Code.

> **Principe :** Plus Claude connaît ton entreprise, plus il devient utile. Ce template te donne la structure pour alimenter Claude au fil du temps.

---

## Démarrage rapide

Tout se fait à partir de **Pilora** et de ton agent (Claude ou Codex). Pas de GitHub, pas de fichier à décompresser.

### Étape 1 : Crée ton compte Pilora
Va sur [pilora.ai](https://www.pilora.ai) et crée ton compte (c'est gratuit). Au premier accès, l'écran **Configure ton agent IA** te guide clic par clic.

### Étape 2 : Branche Pilora sur ton agent
- **Claude** : ajoute Pilora comme connecteur sur claude.ai (Paramètres → Connecteurs → Ajouter un connecteur personnalisé). Pilora te donne l'adresse à coller. Le connecteur apparaît ensuite tout seul dans Claude Code.
- **Codex** : dans l'app Codex, Réglages → Serveurs MCP → Ajouter, colle l'adresse donnée par Pilora, puis clique S'authentifier.

### Étape 3 : Demande ton starter à ton agent
Crée un dossier pour ta business (par exemple **ma-business** sur ton Bureau), ouvre-le dans ton agent (onglet **Code** de l'app Claude, ou comme projet dans Codex), puis écris :

> Installe mon starter Pilora

Ton agent télécharge le starter depuis Pilora et l'installe dans le dossier. Accepte la permission qu'il te demande : c'est un seul fichier.

### Étape 4 : Lance `/demarrer`
Ton agent te pose quelques questions sur ton offre et ton client idéal, enregistre tout dans Pilora, puis te prépare du contenu prêt à publier. Dans Codex, les skills se lancent avec `$` (par exemple `$demarrer`).

**North Star par défaut : générer du revenu rapidement.** Tout est orienté vers ça.

### Mettre à jour ton starter
Quand une nouvelle version sort, Pilora te le dit. Écris à ton agent : « Mets à jour mon starter Pilora ». Il remplace seulement les fichiers gérés par Pilora (skills, agents, prompts) et ne touche jamais à tes fichiers personnels (ton `CLAUDE.md`, ton contexte, ta brand, tes clients). La liste exacte est dans `pilora-starter.json`.

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

Une fois Pilora branché (étape 2), tu n'as rien d'autre à configurer. Tape :
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
├── pilora-starter.json    ← ✅ Version du starter + fichiers gérés / personnels
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
