---
name: montage-video
description: Monter une vidéo courte (reel, short, TikTok) orientée rétention et conversion — de l'idée au fichier exporté. Aide à structurer le script (hook, corps, CTA), à sous-titrer (captions burn-in), à couper les silences et à exporter au bon format. Générique, sans charte de marque imposée. Déclencheurs "monte ma vidéo", "édite ce reel", "sous-titre cette vidéo", "coupe les silences", "prépare un short".
---

# 🎬 Montage vidéo — reels / shorts orientés rétention

> Skill générique : tu montes SES vidéos, dans SON style (lis `docs/brand/voice-tone.md`). Aucune charte imposée. Objectif : des vidéos qui **retiennent l'attention** et **poussent à l'action**, pas des effets pour faire joli.

> **🔒 Accès 10K requis.** La connexion `10k-digital` doit être active avant d'exécuter cette skill (voir `CLAUDE.md` → Étape 0). Vérifie avec `get_my_context` : si l'appel échoue ou que la limite d'abonnement est atteinte, renvoie le membre au login / abonnement et **n'exécute pas** la skill.

## Pré-requis (à vérifier une fois)

```bash
ffmpeg -version   # montage/export/sous-titres
```
Si `ffmpeg` manque : `brew install ffmpeg` (Mac) ou voir ffmpeg.org. Pour la transcription auto des sous-titres, une clé Deepgram/Whisper est optionnelle (sinon, sous-titres manuels).

## Ce que tu produis

De l'idée (ou d'un rush brut) à un fichier `.mp4` vertical prêt à publier, avec sous-titres incrustés.

---

## Étape 1 — Cadrer l'objectif

Demande, en une question : **but de la vidéo** (attirer / éduquer / vendre), **plateforme** (Reels/Shorts/TikTok), et **durée visée**. Rappelle la règle d'or : au-delà de ~60 s, la rétention chute — vise court et dense.

## Étape 2 — Script rétention-first

Structure toute vidéo courte ainsi :

1. **Hook (0–3 s)** — une phrase qui crée une tension ou une promesse claire. Pas d'intro « salut c'est moi ». On entre dans le vif.
2. **Corps** — un seul message, une idée par vidéo. Chaque point avec un **exemple concret** (jamais un concept abstrait nu).
3. **Stimulus visuel ≤ 5 s** — sur TOUTE la vidéo, il se passe quelque chose visuellement au moins toutes les 5 s (zoom, coupe, b-roll, texte à l'écran) pour tenir l'attention. Exception : démonstration d'écran.
4. **CTA (fin, < 5 s)** — une seule action, simple. Pour le trafic organique : subtil (« abonne-toi », « écris-moi »), on ne « vend » pas frontalement.

Écris le script en respectant `docs/brand/voice-tone.md`. Montre-le, itère, puis passe au montage.

## Étape 3 — Préparer les rushes

- Demande le(s) fichier(s) source.
- **Couper les silences / hésitations** (rythme serré) — repérer les blancs et générer les coupes. Exemple ffmpeg pour concaténer des segments gardés :
```bash
# segments.txt : une ligne "file 'clipN.mp4'" par morceau à garder
ffmpeg -f concat -safe 0 -i segments.txt -c copy sortie_coupee.mp4
```
- Garder des **mots entiers** — jamais charcuter au milieu d'un mot.

## Étape 4 — Sous-titres (captions burn-in)

Les captions augmentent la rétention (beaucoup regardent sans son). Deux voies :

**A. Auto (si transcription dispo)** — transcrire l'audio → générer un `.srt` → incruster.
**B. Manuel** — écrire le `.srt` à la main (court, c'est rapide sur une vidéo de < 60 s).

Format `.srt` :
```
1
00:00:00,000 --> 00:00:02,200
Voici le hook
```

Incrustation avec ffmpeg (sous-titres centrés, lisibles, contour pour tenir sur tout fond) :
```bash
ffmpeg -i sortie_coupee.mp4 -vf "subtitles=captions.srt:force_style='Alignment=2,Fontsize=16,PrimaryColour=&Hffffff&,OutlineColour=&H000000&,BorderStyle=1,Outline=2,MarginV=60'" -c:a copy final.mp4
```
Style par défaut : **texte blanc, contour noir, centré-bas**. N'impose pas de couleur de marque sauf si `voice-tone.md` en précise une. Les captions sont un **overlay** par-dessus l'image — jamais une bande qui pousse le contenu.

## Étape 5 — Format & export

- **Vertical 9:16 = 1080×1920** pour Reels/Shorts/TikTok.
- Recadrer un rush horizontal si besoin :
```bash
ffmpeg -i entree.mp4 -vf "scale=-1:1920,crop=1080:1920" -c:a copy vertical.mp4
```
- Export final H.264, audio AAC, débit propre :
```bash
ffmpeg -i final.mp4 -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k export.mp4
```

## Étape 6 — Livrer

Montre le fichier final au membre (chemin), propose 2-3 titres + une légende de publication cohérents avec son style, et note dans `ai/memory/in-progress.md` si une série est en cours.

---

## Règles

- **Rétention avant tout** : si un effet n'aide pas à retenir ou à comprendre, on l'enlève.
- Respecter `docs/brand/voice-tone.md` pour le ton, les mots, la langue.
- Montrer le script avant de monter ; montrer le résultat avant de dire « c'est fait ».
- Ne jamais publier à la place du membre sans son feu vert explicite.
