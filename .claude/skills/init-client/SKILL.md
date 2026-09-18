---
name: init-client
description: Use when onboarding a new client — asks 5 questions and generates a complete client file in docs/clients/
---

# Init Client

> **Connexion 10K.** Cette skill donne son plein résultat branchée au compte du membre. S'il n'est pas encore connecté (voir `CLAUDE.md` → Démarrage), propose-lui gentiment de brancher son 10K en un clic (`/mcp` → `10k-digital`) — sans le braquer.

## What it does

Guides you through 5 questions about a new client and automatically generates a complete client file in `docs/clients/[client-name].md` using the standard template.

---

## Process

### Step 1 — Read context
Before starting, read:
- `CLAUDE.md` — tone and absolute rules
- `docs/clients/_template.md` — the template to use

### Step 2 — Ask 5 questions (one at a time)

Ask these questions one by one, wait for each answer before asking the next:

1. **Nom complet et entreprise** : "Quel est le nom complet du client et le nom de son entreprise ?"
2. **Offre achetée et prix** : "Quelle offre a-t-il achetée, et à quel prix ?"
3. **Objectif principal** : "Quel est son objectif principal — ce qu'il veut atteindre grâce à cette offre ?"
4. **Contexte de son entreprise** : "Décris-moi sa situation actuelle en 2-3 phrases (revenus, stade, défis)."
5. **Notes importantes** : "Y a-t-il des préférences, contraintes ou infos importantes à noter sur ce client ? (communication, disponibilités, points sensibles...)"

### Step 3 — Generate the file

Using the answers collected:
1. Create the file `docs/clients/[nom-client-kebab-case].md`
2. Fill in all sections from `docs/clients/_template.md`
3. Set the creation date to today
4. Set status to "Actif"
5. Add a first entry in "Historique des interactions" : "Onboarding — client ajouté au système"

### Step 4 — Confirm

Tell the user:
- The file path created
- A summary of what was captured
- Suggest the next step: "Tu peux maintenant taper `/weekly-review` pour inclure ce client dans ta revue hebdomadaire."

---

## Rules

- Ask questions ONE AT A TIME — never batch them
- Use the client's exact words when filling in the file (don't rephrase their goals)
- If the user skips a question, leave the field as `[À remplir]` — never invent information
- Always confirm the file was created before ending
