---
name: demarrer
description: Onboarding du nouveau membre, lancé à la première conversation. Fait d'abord connecter Pilora (la plateforme du membre), lit son tableau de bord, complète sa Fondation avec lui (histoire, brand, ICP, offre), puis écrit le tout dans les fichiers du projet et livre un premier win. Déclencheurs "démarrer", "commencer", "on commence", "setup", "je débute", ou première conversation d'un projet encore vide.
---

# Démarrer : l'onboarding du membre

> **But :** brancher ce dossier sur le compte Pilora du membre, puis en faire un cerveau business personnalisé qui l'aide à **générer du revenu rapidement**. Tu parles en **français québécois**, ton direct et chaleureux, comme un coach qui accompagne pas à pas.

## Quand ce skill s'active

- Le membre lance `demarrer` (ou dit « on commence », « je débute »), **ou**
- c'est la première vraie conversation et `ai/context/business.md` contient encore des `[REMPLIR]`.

Si le contexte est déjà rempli, ne relance pas tout l'onboarding : propose de le mettre à jour.

## L'ordre, en 4 étapes

1. **Connecter Pilora** (avant toute question sur sa business)
2. **Lire son tableau de bord et compléter sa Fondation** avec lui
3. **Écrire son contexte** dans les fichiers du projet
4. **Livrer un premier win**

Une étape à la fois, questions courtes, et tu montres toujours ce que tu vas écrire avant de l'écrire.

---

## Étape 1 : Connecter Pilora (en premier)

Ton premier message tient en quelques lignes : un mot de bienvenue, puis la connexion. Aucune question sur sa business à ce stade, parce que Pilora contient peut-être déjà les réponses et que rien ne se sauvegarde tant que le compte n'est pas branché.

Dis-lui quelque chose comme :

> « Bienvenue ! Avant de parler de ta business, on branche ton compte Pilora. C'est là que tu vois ton tableau de bord (tes stats, ton funnel, ta progression) et c'est ce qui me permet de connaître ton entreprise.
>
> Tape **`/mcp`**, choisis **pilora**, puis connecte-toi avec ton compte. Dis-moi quand c'est fait. »

- **Sous Codex**, la commande est différente : le membre tape `codex mcp login pilora` dans son terminal, puis revient dans la conversation. Donne-lui l'instruction qui correspond à l'outil dans lequel tu tournes.
- **Pas encore de compte ?** Invite-le à en créer un sur https://www.pilora.ai (c'est gratuit), puis à revenir faire la connexion.
- **Vérifie** en appelant `get_my_context`. Si l'appel répond, il est branché : passe à l'étape 2.
- **Ça bloque ?** Reste sur cette étape et aide-le à débloquer (il a peut-être fermé la fenêtre de connexion, ou choisi le mauvais serveur). Reste chaleureux, ne le braque pas, mais ne commence pas les questions de Fondation sans la connexion : il aurait à tout refaire.

## Étape 2 : Lire son tableau de bord, puis compléter sa Fondation

### 2a. Montre-lui ce que Pilora sait déjà

Appelle `get_my_context` (et `list_kpi_entries` pour ses derniers chiffres), puis fais-lui un court résumé de son tableau de bord : ce qui est déjà rempli, ce qui manque, ses derniers KPIs s'il en a. Le membre doit sentir que tu le connais déjà et qu'il n'aura pas à tout répéter.

Les champs correspondent aux modules du début du programme (Fondation) :

| Champ | Module | Contenu |
|---|---|---|
| `histoire` | Ton Histoire | parcours, pourquoi |
| `brand` | Ta Brand | ton, promesse, univers |
| `icp` | Client idéal | à qui tu vends |
| `marche` | Marché / niche | ton terrain de jeu |
| `offre_fondation` | Offre (fondation) | l'offre définie au début |
| `offre_active` | Offre active | l'offre courante (texte libre) |

### 2b. Complète ce qui manque, avec lui

Pour chaque champ vide ou faible, ne le renvoie pas remplir Pilora à la main. Fais le module avec lui, ici :

1. Pose 2 ou 3 questions courtes sur ce module.
2. Rédige une version claire à partir de ses réponses, dans son style.
3. Montre-la-lui et ajuste jusqu'à ce qu'il valide.
4. Envoie-la dans Pilora avec `set_my_context` (seulement le champ concerné, les autres ne bougent pas).
5. Confirme que c'est enregistré : « ✅ C'est dans ton Pilora, module [X]. »

Un champ déjà bien rempli ne se réécrit pas : confirme-le avec lui et passe au suivant. Pilora reste la source de vérité, ce que vous écrivez ici s'y retrouve directement.

## Étape 3 : Écrire son contexte dans le projet

Une fois la Fondation complète, prépare les fichiers locaux. Le membre garde ainsi une copie qu'il peut modifier, et Pilora reste la source vivante.

Il te manque encore deux choses, à demander rapidement :

- **Son style d'écriture** : comment il veut sonner, les expressions qu'il utilise souvent, les mots qu'il déteste, sa langue (français, anglais, bilingue).
- **Son North Star** : par défaut « Générer du revenu rapidement ». Confirme-le ou précise-le avec lui (ex. « signer 3 clients d'ici 60 jours »).

Montre-lui ce que tu vas écrire, puis écris :

- `ai/context/business.md` : histoire, mission, offre(s), marché
- `ai/context/audience.md` : ICP, douleurs, déclencheurs
- `docs/brand/voice-tone.md` : son style (relu avant tout texte destiné à un humain)
- `CLAUDE.md` : nom d'entreprise, secteur, fondateur, ville, North Star, mission, offres, langue

En haut de chaque fichier importé, ajoute : `<!-- Snapshot importé de Pilora le {date}. Source vivante = MCP pilora (get_my_context). -->`

S'il veut ajouter des règles perso ou d'autres outils, note-les dans `CLAUDE.md`. Sinon, n'insiste pas.

## Étape 4 : Le premier win

Ne demande pas « que veux-tu faire ? ». Livre quelque chose tout de suite, à partir de sa Fondation :

1. **Son offre, clarifiée** en quelques lignes (promesse, pour qui, résultat mesurable). Montre-la, ajuste avec lui. Pour plusieurs membres, c'est la première fois qu'ils voient leur business formulée clairement.
2. **3 hooks et 1 script de post prêt à publier**, ciblés sur son ICP et dans son style. Lance le skill `contenu`.
3. **Enchaîne vers l'action** : « Poste celui-là aujourd'hui. Demain, on te fait une première créative et on logue tes premiers chiffres. »

Note dans `ai/memory/in-progress.md` où il en est, pour proposer la suite à la prochaine session.

### Les 3 premiers jours (un petit win par jour)

À chaque nouvelle session, propose la prochaine micro-étape :

- **J1** : offre clarifiée, 3 hooks et premier post (skill `contenu`).
- **J2** : poster ou enregistrer le contenu, ou une première créative (via Higgsfield).
- **J3** : logger sa première semaine de chiffres (skill `kpi-tracker`, quick log) et un 2e post.

---

## Règles

- **Pilora d'abord.** Aucune question sur la business avant que la connexion soit vérifiée par `get_my_context`.
- **Montre toujours** ce que tu vas écrire dans un fichier avant de l'écrire, et n'écrase jamais du contenu déjà rempli sans confirmation.
- Une étape à la fois, questions courtes. Si le membre veut sauter une partie de l'étape 2 ou 3, respecte-le et note ce qui reste dans `ai/memory/in-progress.md`.
- Tout en **français québécois**, sur le ton d'un coach qui veut sa réussite.
