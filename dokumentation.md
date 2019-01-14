---
title: Dokumentation des Programmentwurfs
author: Niklas Jaeger, Arian Moser
header:
    - left: Wissensbasierte Systeme
    - center: Evidenztheorie / Dempster Regel
    - right: 14.01.2019
footer: yes
titlepage: yes
---

# Dokumentation des Programmentwurfs: Erkennung einer Emotion anhand von Sprache

## Beschreibung

### Einzusetzende Methode: 
Evidenztheorie / Dempster Regel

### Gegebene Informationen: 
- CSV Datei mit struktuierten Daten
- Liste von Sprechdaten taktweise

### Gegebene Features
- Sprechgeschwindigkeit (langsamer, normal, schneller)
- durchschnittliche Tonlage (niediger, normal, höher)
- Schallstärke/Intensität (schwächer, normal, stärker)

### Mögliche Emotionen
- Ekel
- Freude
- Angst 
- Überraschung
- Wut
- Traurigkeit

### Rückschluss von Feature auf Emotion
#### Sprechgeschwindigkeit
- Langsam:
    - Ekel, Freude
- Schnell:
    - Angst, Überraschung, Wut, Freude
#### Tonlage
- Tief:
    - Ekel, Traurigkeit
#### Schallstärke (Intensität)
- Schwach
    - Traurigkeit, Ekel
- Stark
    - Wut, Freude, Überraschung

### Aufgabe 
- Analyse, Modellierung und Verarbeitung mittels Evidenztheorie

## Vorgehensweise








