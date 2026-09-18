---
name: demarrer
description: Onboarding du nouveau membre — se lance à la première conversation. Connecte le MCP 10K, tire le contexte business de l'app (histoire, brand, ICP, offre), fait compléter ce qui manque, définit le style d'écriture, et écrit tout ça dans les fichiers du projet. North Star par défaut = générer du revenu rapidement. Déclencheurs : "démarrer", "commencer", "on commence", "setup", "je débute", ou première conversation d'un projet encore vide.
---

# 🚀 Démarrer — Onboarding du membre

> **But :** transformer ce dossier vide en cerveau business personnalisé, pour que Claude devienne immédiatement utile à faire **du revenu rapidement**. Tu parles en **français québécois**, ton direct et chaleureux, comme un coach qui accompagne pas à pas.

## Quand ce skill s'active

- Le membre tape `/demarrer` (ou dit « on commence », « je débute »), **ou**
- C'est la première vraie conversation et `ai/context/business.md` contient encore des `[REMPLIR]` / `CLAUDE.md` n'est pas personnalisé.

Ne relance pas l'onboarding complet si le contexte est déjà rempli — propose plutôt de le mettre à jour.

## Principe

Tu ne poses PAS 40 questions. Une grande partie du contexte (histoire, brand, ICP, offre, marché) est **déjà remplie par le membre dans l'app 10K Digital** (modules du début). Ton travail : **tirer ça de l'app**, puis ne demander en chat que ce qui manque. Toujours **montrer avant d'écrire** dans un fichier.

---

## Étape 1 — Accueil chaleureux (30 secondes)

Souhaite la bienvenue, ton d'un coach qui veut sa réussite. Explique en 3 phrases :
1. Ce dossier, c'est le **cerveau** de sa business — plus il le nourrit, plus Claude devient précis.
2. On va brancher son **tableau de bord 10K Digital** : c'est là qu'il verra ses **stats, son funnel et sa progression**, et ça permet à Claude de connaître sa business.
3. Objectif par défaut : **générer du revenu le plus vite possible** (on ajustera).

Puis enchaîne en douceur sur l'étape 2.

## Étape 2 — Brancher son tableau de bord 10K

C'est ce qui relie ton Claude à SON compte. Amène-l'y **tôt et avec le sourire**, comme un bénéfice (« on branche ton tableau de bord pour voir tes stats et sauvegarder ton travail »), jamais comme un péage.

1. **Compte :** s'il n'a pas encore de compte 10K, invite-le gentiment à en créer un (gratuit) dans l'app 10K, puis à revenir.
2. **Connexion :** le MCP est déjà pré-configuré (`.mcp.json`). Guide-le :
   > « Tape **`/mcp`**, choisis **10k-digital**, et connecte-toi. C'est un clic. Dis-moi quand c'est fait. »
3. **Vérifie** avec `get_my_context`.
   - Si ça marche → enchaîne sur l'étape 3.
   - Si pas encore connecté → **ne le braque pas** : ré-explique la valeur en une phrase (« c'est ce qui sauvegarde ta Fondation et te donne ta plateforme »), et aide-le à brancher. Tu peux discuter et le préparer en attendant, mais rappelle que rien ne se sauvegarde tant que ce n'est pas branché.

## Étape 3 — Compléter la Fondation (Stratégie du début) AVEC le membre, puis sync vers l'app

Lis ce que `get_my_context` renvoie. Les champs correspondent aux modules du **début du programme (Stratégie / Fondation)** :

| Champ contexte | Module | Contenu |
|---|---|---|
| `histoire` | Ton Histoire | parcours, pourquoi |
| `brand` | Ta Brand | ton, promesse, univers |
| `icp` | Client idéal | à qui tu vends |
| `marche` | Marché / niche | ton terrain de jeu |
| `offre_fondation` | Offre (fondation) | l'offre définie au début |
| `offre_active` | Offre active | l'offre courante (texte libre) |

Pour **chaque champ vide ou faible**, ne renvoie PAS le membre remplir l'app à la main. **Fais le module avec lui, ici :**

1. Pose 2-3 questions courtes pour ce module (une chose à la fois).
2. Rédige une version claire à partir de ses réponses, dans SON style.
3. **Montre-la-lui** et ajuste jusqu'à ce qu'il valide.
4. **Sync vers l'app** avec `set_my_context` — uniquement le(s) champ(s) concerné(s), les autres ne bougent pas.
5. Confirme que c'est enregistré (« ✅ synchronisé dans ton app, module [X] »).

Enchaîne module par module jusqu'à ce que la Fondation soit complète. L'app reste la **source de vérité partagée** : ce que vous écrivez ici la remplit directement, le membre n'a rien à re-saisir ailleurs.

> Si un champ est **déjà bien rempli** dans l'app, ne le réécris pas : confirme-le avec le membre et passe au suivant.

## Étape 4 — Importer le contexte (snapshot local + MCP live)

Une fois le contexte disponible via `get_my_context`, écris-en un **snapshot** dans les fichiers (le membre garde une copie éditable, hors-ligne ; le MCP reste la source vivante qu'on rafraîchit sur demande). **Montre-lui d'abord** ce que tu vas écrire, puis écris :

- `ai/context/business.md` → histoire, mission, offre(s), marché
- `ai/context/audience.md` → ICP / avatars, douleurs, déclencheurs
- `CLAUDE.md` → remplir l'en-tête : nom d'entreprise, secteur, fondateur, ville, **North Star**, mission, offres, langue

Ajoute en haut de chaque fichier importé une ligne : `<!-- Snapshot importé de l'app 10K le {date}. Source vivante = MCP 10k-digital (get_my_context). -->`

## Étape 5 — Définir le style d'écriture (son « MyStyle » à lui)

C'est SON style, pas celui de quelqu'un d'autre. Pose 3-4 questions courtes :
1. Comment tu veux sonner ? (ex. direct, chaleureux, expert, cash)
2. Des mots/expressions que tu utilises tout le temps ?
3. Des mots/tics que tu détestes et qu'on bannit ?
4. Langue : français, anglais, bilingue ?

Écris le résultat dans `docs/brand/voice-tone.md` (montre avant d'écrire). Ce fichier sera relu avant tout texte destiné à un humain.

## Étape 6 — North Star

Par défaut : **« Générer du revenu rapidement »**. Confirme-le avec lui, ou précise-le (ex. « signer 3 clients DFY d'ici 60 jours »). Écris-le dans `CLAUDE.md`.

## Étape 7 — Compléter les trous en chat

Ce qui n'est ni dans l'app ni encore couvert (règles absolues perso, outils/MCP en plus, offres secondaires) : demande-le brièvement et écris-le au bon endroit.

## Étape 8 — Récap + première action orientée revenu

Résume ce qui a été rempli, ce qui reste à compléter (le cas échéant), et **propose immédiatement une première action concrète qui rapproche du revenu** — par exemple :
- « Veux-tu que je t'écrive 3 hooks pour ton offre principale ? »
- « On prépare ton prochain appel de vente ? »
- « Je log tes chiffres de la semaine dans ton tableau 10K avec `/kpi-tracker` ? »

---

## Règles

- **Montre toujours** ce que tu vas écrire dans un fichier AVANT de l'écrire ; ne jamais écraser du contenu déjà rempli sans confirmation.
- Ne submerge pas : une étape à la fois, questions courtes.
- Si le membre veut sauter une étape, respecte-le et note ce qui reste à faire dans `ai/memory/in-progress.md`. **L'étape 2 (brancher le 10K) donne la vraie valeur** : amène-l'y tôt et avec douceur, rappelle que rien ne se sauvegarde sans elle, mais ne refuse jamais sèchement.
- Tout en **français québécois**, ton d'un coach qui veut sa réussite.
