---
name: weekly-review
description: Use at the end of each week — reads business context files and generates a structured review with wins, blockers, and next week priorities
---

# Weekly Review

## What it does

Reads your current business state and generates a structured weekly review with wins, blockers, and your top 3 priorities for next week.

---

## Process

### Step 1 — Read these files (in order)

1. `ai/memory/in-progress.md` — current tasks and blockers
2. `docs/finance/metrics.md` — revenue and key metrics
3. `ai/agents/sales/context.md` — pipeline status
4. `ai/agents/marketing/context.md` — marketing performance
5. `ai/agents/fulfillment/context.md` — active client delivery status

### Step 2 — Ask one question

Before generating the report, ask:

> "Y a-t-il des événements importants de la semaine que je dois savoir avant de générer le rapport ? (nouveaux clients, problèmes, victoires, décisions importantes)"

Wait for the answer.

### Step 3 — Generate the weekly review

Use this format:

---

## Revue Hebdomadaire — Semaine du [DATE]

### ✅ Victoires de la semaine
*(Ce qui a bien marché — minimum 3 items même si petits)*
- [win 1]
- [win 2]
- [win 3]

### 🔴 Blocages & problèmes
*(Ce qui a freiné l'avancement)*
- [blocage 1] → Action suggérée : [action]
- [blocage 2] → Action suggérée : [action]

### 📊 Métriques clés
| Métrique | Cette semaine | Tendance |
|----------|---------------|----------|
| MRR | [valeur] | [↑/↓/→] |
| Pipeline actif | [valeur] | [↑/↓/→] |
| Clients actifs | [valeur] | [↑/↓/→] |

### 🎯 Top 3 priorités — Semaine prochaine
1. **[PRIORITÉ 1]** — Pourquoi : [raison] — Action : [action concrète]
2. **[PRIORITÉ 2]** — Pourquoi : [raison] — Action : [action concrète]
3. **[PRIORITÉ 3]** — Pourquoi : [raison] — Action : [action concrète]

### 💡 Insight de la semaine
[Une observation stratégique basée sur les données — ce que les chiffres indiquent]

---

### Step 4 — Update in-progress

After generating the report, suggest:

> "Veux-tu que je mette à jour `ai/memory/in-progress.md` avec les priorités de la semaine prochaine ?"

If yes, update the file with the top 3 priorities as the new "Prochaines étapes".

---

## Rules

- If files are empty or incomplete, note it in the report: "Données manquantes — remplir [fichier] pour de meilleures analyses"
- Never invent metrics — use only what's in the files
- Priorités must be actionable (verb + object + deadline), not vague goals
- Always end with one concrete insight, not just a summary
