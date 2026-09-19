---
name: debloquer
description: Débloque le bundle de skills premium (programme DFY 4k). Vérifie l'abonnement via le MCP 10K et installe les skills premium seulement si le membre est client DFY. Déclencheurs "débloque le bundle", "installer les skills premium", "j'ai pris le 4k", "unlock", "mes skills premium".
---

# Débloquer — le bundle premium (programme DFY 4k)

> Réservé aux clients du programme **DFY 4k**. La vérification se fait **côté serveur** (MCP 10K) : rien à contourner en local.

## Étape 1 — Vérifier le tier

Assure-toi que le 10K est branché (`/mcp` → `10k-digital`), puis appelle l'outil MCP **`get_my_subscription`**.

- Tier **`dfy`** → passe à l'étape 2.
- Tier `free` ou `active` → **n'installe rien.** Explique chaleureusement : « Le bundle premium (créatives via Higgsfield, gestion d'ads Meta, analyse concurrents, media-buying…) fait partie du programme DFY 4k. Si tu veux l'ajouter à ton système, parle-en à ton coach. » Ne braque pas, propose la valeur.

## Étape 2 — Récupérer le bundle (source gatée)

Pour un membre `dfy`, appelle l'outil MCP **`get_premium_bundle_url`** — il renvoie un **lien de téléchargement signé et temporaire**, émis uniquement aux clients DFY.

1. Télécharge le ZIP du bundle depuis ce lien.
2. Extrais les skills dans **`.claude/skills/`**. **Ne remplace jamais une skill existante sans confirmer.**
3. Confirme la liste installée.

> **Si `get_premium_bundle_url` n'existe pas encore** (infra bundle non déployée) : dis au membre que son bundle premium lui sera **livré par son coach**, et note-le dans `ai/memory/in-progress.md`. **Ne bricole jamais une source publique** — les skills premium ne doivent jamais fuiter hors des clients DFY.

## Étape 3 — Confirmer

Liste les nouvelles skills disponibles et propose la première action utile (ex. « on te génère ta première créative d'ad ? »).

## Règles

- **Jamais** d'installation sans un tier `dfy` confirmé par le MCP.
- **Jamais** de lien de téléchargement codé en dur : il vient toujours de l'outil MCP (signé, temporaire).
- Montre ce que tu vas installer avant de le faire.
