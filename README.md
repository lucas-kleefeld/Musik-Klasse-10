# Musik Klasse 10 – Notenlehre

Lerntexte, Übungen und Werkzeuge zur Notenlehre für den Musikkurs Klasse 10. Die Reihe wiederholt die Theorie aus den Klassen 7 bis 9 in aufsteigender Folge und schließt mit dem Quintenzirkel ab.

Die Website: `index.html` (über GitHub Pages veröffentlicht).

## Aufbau der Reihe

| Stufe | Kapitel | Inhalt | Herkunft |
|---|---|---|---|
| 1 Rhythmus | 1 Notenwerte und Takt | Ganze bis Sechzehntel, Notenbaum, Taktarten, Zählen, Auftakt | Klasse 7 |
| | 2 Pausen | Pausenwerte, Lage im System, Ganztaktpause | Klasse 7 |
| | 3 Punktierte Noten und Triolen | Punktierung, typische Rhythmen, Achtel- und Vierteltriolen | Klasse 7 |
| 2 Tonhöhe und Lautstärke | 4 Noten im Violinschlüssel | Notensystem, Stammtöne c′ bis a″, Oktavbereiche, Hilfslinien, Halsrichtung, Klaviatur | Klasse 7 |
| | 5 Vorzeichen | Kreuz, b, Auflösungszeichen, Tonnamen, Gültigkeit, Generalvorzeichen, enharmonische Verwechslung | Klasse 8 |
| | 6 Dynamik | ppp bis fff, crescendo, decrescendo, sforzato, Akzent | Klasse 8 |
| 3 Tonleitern | 7 Ganz- und Halbtöne, Dur-Tonleiter | Halbton, Ganzton, Bauplan Dur, Dur-Tonleitern bilden, Tonart, Tetrachorde | Klasse 8 |
| | 8 Moll-Tonleitern | natürliches, harmonisches, melodisches Moll, Paralleltonarten | Klasse 8 |
| 4 Intervalle und Dreiklänge | 9 Intervalle | Prime bis Oktave, rein/groß/klein, bestimmen und notieren | Klasse 9 |
| | 10 Dreiklänge | Terzschichtung, Dur/Moll/vermindert/übermäßig, Akkordsymbole, Hauptdreiklänge, Umkehrungen | Klasse 8 |
| 5 Quintenzirkel | 11 Der Quintenzirkel | Herleitung über Tetrachorde, Kreuz- und b-Tonarten, Reihenfolge der Vorzeichen, Tonart bestimmen, Abschlusstest | Klasse 10 |

Die Intervalle stehen vor den Dreiklängen, weil die Terzschichtung große und kleine Terzen voraussetzt.

Zu jedem Kapitel gibt es

- einen **Lerntext** mit Notenbeispielen zum Anhören,
- **Aufgaben** als druckbares Arbeitsblatt (AFB I bis III, mit Notenzeilen),
- **Übungen** mit sofortiger Rückmeldung: Notenquiz, Noten lesen, Noten per Klick notieren, Halbtöne markieren, Zuordnen, Sortieren, Reihenfolge.

Dazu kommen vier **Werkzeuge**: Klaviatur, interaktiver Quintenzirkel, Taktbaukasten und Notentrainer (Zufallsaufgaben).

„Prüfen“ und „Lösung zeigen“ werden erst freigegeben, wenn eine Übung vollständig bearbeitet ist. Beim Quiz gibt es die Rückmeldung direkt nach jeder beantworteten Frage.

## Kapitel freischalten (für Lehrkräfte)

Welche Kapitel Schülerinnen und Schüler sehen, steht in der Datei [`freigabe.json`](freigabe.json):

1. Auf GitHub die Datei `freigabe.json` öffnen und auf den Stift („Edit this file“) klicken.
2. Beim gewünschten Kapitel `true` (frei) oder `false` (gesperrt) eintragen.
3. Unten auf „Commit changes“ klicken.

Danach erzeugt GitHub die Seiten automatisch neu (Reiter „Actions“), nach etwa zwei Minuten ist die Änderung online. Gesperrte Kapitel werden gar nicht als Seiten veröffentlicht. Hinweis: Weil das Repository öffentlich ist, bleiben die Quelltexte im Ordner `werkzeug/` auf GitHub einsehbar.

## Seiten neu erzeugen

Alle HTML-Seiten entstehen aus den Python-Dateien in `werkzeug/` (Inhalte in `kap_*.py`). Für den Notensatz wird Node.js benötigt. Aufruf: `cd werkzeug && python3 bauen.py`.

## Datenschutz und Urheberrecht

- Keine externen Inhalte, keine Datenspeicherung, keine Anmeldung. Der Klang wird im Browser erzeugt (Web Audio).
- Texte, Aufgaben, Zeichnungen und Programmcode sind eigens erstellt. Die Notenbeispiele sind eigene Beispiele oder gemeinfreie Tonfolgen; Liedtitel werden nur als Hörhilfe genannt.
- Notenzeichen: Schrift Bravura (Steinberg) unter der SIL Open Font License (`assets/OFL-Bravura.txt`). Schriften Atkinson Hyperlegible, Bricolage Grotesque und Caveat ebenfalls unter der SIL Open Font License (`assets/fonts/`).
