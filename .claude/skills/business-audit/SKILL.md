---
name: business-audit
description: Use when you need a full business health check — reads all context files, identifies gaps and missing information, and generates prioritized recommendations
---

# Business Audit

> **🔒 Accès 10K requis.** La connexion `10k-digital` doit être active avant d'exécuter cette skill (voir `CLAUDE.md` → Étape 0). Vérifie avec `get_my_context` : si l'appel échoue ou que la limite d'abonnement est atteinte, renvoie le membre au login / abonnement et **n'exécute pas** la skill.

## What it does

Reads all your business context files, identifies what's missing, what's weak, and what's strong — then delivers a prioritized action plan.

---

## Process

### Step 1 — Read ALL context files

Read every file in this order:
1. `CLAUDE.md`
2. `ai/context/business.md`
3. `ai/context/audience.md`
4. `docs/brand/voice-tone.md`
5. `docs/brand/positioning.md`
6. `docs/brand/offers.md`
7. `ai/agents/marketing/context.md`
8. `ai/agents/sales/context.md`
9. `ai/agents/fulfillment/context.md`
10. `docs/finance/metrics.md`
11. `docs/clients/` — scan all client files

Count:
- How many `[REMPLIR]` fields are still empty?
- Which sections are partially filled vs fully filled?

### Step 2 — Generate the audit report

Use this format:

---

## Audit Business — [DATE]

### 📋 État de la documentation

| Fichier | Statut | Champs manquants |
|---------|--------|-----------------|
| CLAUDE.md | [🟢 Complet / 🟡 Partiel / 🔴 Vide] | [liste] |
| ai/context/business.md | [🟢/🟡/🔴] | [liste] |
| ai/context/audience.md | [🟢/🟡/🔴] | [liste] |
| docs/brand/ | [🟢/🟡/🔴] | [liste] |
| docs/finance/metrics.md | [🟢/🟡/🔴] | [liste] |

**Score de complétion : [X]% des champs remplis**

---

### 💪 Points forts identifiés
*(Ce qui est bien documenté et qui peut être utilisé immédiatement)*

- [force 1]
- [force 2]

### ⚠️ Gaps critiques
*(Ce qui manque et qui limite ce que Claude peut faire pour toi)*

- [gap 1] → Impact : [pourquoi c'est bloquant]
- [gap 2] → Impact : [pourquoi c'est bloquant]

### 💡 Opportunités identifiées
*(Ce que les données suggèrent comme piste d'action)*

- [opportunité 1]
- [opportunité 2]

### 🎯 Plan d'action — 3 étapes prioritaires

**Étape 1 (faire maintenant — <30 min) :**
Remplir [fichier(s) critique(s)] — spécifiquement les sections [sections].

**Étape 2 (cette semaine) :**
[Action concrète basée sur les gaps identifiés]

**Étape 3 (ce mois) :**
[Action stratégique plus large]

---

### Step 3 — Offer next steps

After the audit, offer:

> "Veux-tu qu'on remplisse ensemble les gaps les plus critiques ? Je peux te poser les questions et remplir les fichiers au fur et à mesure."

---

## Rules

- Be direct about gaps — don't soften the assessment
- Prioritize by IMPACT: what missing info limits Claude the most?
- If business.md is empty, that's always Gap #1 — nothing works without it
- Score honestly: a file with 3 of 20 fields filled = 🔴, not 🟡
- Opportunities must be based on actual data, not generic advice
