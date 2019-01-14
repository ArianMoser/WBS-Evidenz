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

# Erkennung einer Emotion anhand von Sprache


## Aufgabenstellung

### Einzusetzende Methode: 
Evidenztheorie / Dempster Regel

---

### Gegebene Informationen: 
- CSV Datei mit strukturierten Daten
- Liste von Sprechdaten taktweise

---

### Gegebene Features
- Sprechgeschwindigkeit (langsamer, normal, schneller)
- durchschnittliche Tonlage (niedriger, normal, höher)
- Schallstärke/Intensität (schwächer, normal, stärker)

---

### Mögliche Emotionen
- Ekel
- Freude
- Angst 
- Überraschung
- Wut
- Traurigkeit

---

### Rückschluss von Feature auf Emotion

#### Sprechgeschwindigkeit
- Langsam:
    - Ekel, Freude
- Schnell:
    - Angst, Überraschung, Wut, Freude 

#### Tonlage
- Tief:
    - Ekel, Traurigkeit
- Hoch:
    - Angst, Überraschung, Wut, Freude

#### Schallstärke (Intensität)
- Schwach
    - Traurigkeit, Ekel
- Stark
    - Wut, Freude, Überraschung

---

### Aufgabe 
- Analyse, Modellierung und Verarbeitung mittels Evidenztheorie

\newpage

## Vorgehensweise

### Analyse

Bei der Analyse der gegebenen Informationen fällt auf, dass die
Sprechgeschwindigkeit anstatt in Abstufungen (langsam, mittel, schnell) in
Silben pro Sekunde angegeben ist. Deshalb muss zunächst definiert werden, für
welche Intervalle welche Abstufung zu wählen ist:

| Abstufung\\Geschwindikeit | Von | Bis|
|---:|:---:|:---:|
| **Sehr langsam** | 0 | 3|
| **Langsam** | 3 | 4|
| **Normal** | 4 | 5|
| **Schnell** | 5 | 6 |
| **Sehr schnell** | 6 | |

Da für die anderen beiden Kategorie jeweils direkt die Abstufungen angegeben
sind, muss hier keine extra Einteilung mehr vorgenommen werden.


Im nächsten Schritt geht es an die Ermittlung des Basismaß. Dafür muss für jede
Kategorie in jeder Abstufung ein Plausibilitätswert im Bezug auf die Emotionen
festgesetzt werden.


| Abstufung \\ Kategorie | Sprechgeschwindigkeit | Tonlage      | Schallstärke |
| ---:|:---|:---|:---|
| **sehr niedrig**      | Pl({D})=0.5           | Pl({D})=0.5  | Pl({D,Sa})=0.9   |
|                       | Pl({J})=0.4           | Pl({Sa})=0.35| Pl({O})=0.1   |
|                       | Pl({O})=0.1           | Pl({O})=0.15 |              |
|                       |                       |              |              | 
| **niedrig**           | Pl({D})=0.4           | Pl({D})=0.45 | Pl({D,Sa})=0.8   |
|                       | Pl({J})=0.35          | Pl({Sa})=0.3 | Pl({O})=0.2  |
|                       | Pl({O})=0.25          | Pl({O})=0.25 |              |
|                       |                       |              |              | 
| **normal**            | Pl({O})=1.0           | Pl({O})=1.0  | Pl({O})=1.0  |
|                       |                       |              |              |
| **hoch**              | Pl({J,F,Su,A})=0.8    | Pl({J,F,Su,A})=0.8| Pl({J,Su,a})=0.8   |
|                       | Pl({O})=0.2           | Pl({O})=0.2  | Pl({O})=0.2   |
|                       |                       |              |              |
| **sehr hoch**         | Pl({J,F,Su,A})=0.9    | Pl({J,F,Su,A})=0.9| Pl({J,Su,a})=0.9 |
|                       | Pl({O})=0.1           | Pl({O})=0.1  | Pl({O})=0.1  |
|                       |                       |              |              |


##### Legende:  


| Buchstabe | Emotion |
|---:|:---|
| D  | Ekel| 
| J  | Freude| 
| Sa | Traurigkeit| 
| Su | Überraschung| 
| F  | Angst| 
| A  | Wut| 
| O  | Omega| 

---

### Umsetzung

Im ersten Schritt der Implementierung geht es an das Einlesen der CSV-Datei und
der sinnvollen Speicherung der darin enthalten Daten. Für das Einlesen wurde
auf die Bibliothek *csv* zurückgegriffen. Diese kann CSV-Dateien öffnen und
anhand eines Delimiters deren Daten trennen.  
Danach müssen die Daten noch sinnvoll gespeichert werden. Dafür benutzen wir
übersichtshalber ein Dictionary-Array, indem jede Zeile einen Takt darstellt.
Nach der Eingabe müssen die Daten noch verarbeitet werden. Dabei werden die
einzelnen Abstufungen anhand der obrigen Tabelle in die jeweiligen Evidenzen
m1, m2 und m3 überführt (durch die "MassFunction" aus der Biblothek *pyds*). Im
Anschluss müssen die Evidenzen noch akkumuliert werden. Dies geschieht durch
die Funktion "combine\_conjunctive", welche auch von der Bibliothek *pyds*
mitgeliefert wird.  
Abschließend wird noch die plausibelste Emotion ausgewählt (durch die Funktion
"max\_pl" von *pyds*) und der dazugehörige Wert bestimmt.

---

### Zusätzlich

Github: [ArianMoser/WBS-Evidenz](https://github.com/ArianMoser/WBS-Evidenz)



