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
| | 5 Noten im Bassschlüssel | F-Schlüssel, großes C bis c′, große und kleine Oktave, Merksätze, Vergleich mit dem Violinschlüssel, Klaviersystem | Klasse 8 |
| | 6 Vorzeichen | Kreuz, b, Auflösungszeichen, Tonnamen, Gültigkeit, Generalvorzeichen, enharmonische Verwechslung | Klasse 8 |
| | 7 Dynamik | ppp bis fff, crescendo, decrescendo, sforzato, Akzent | Klasse 8 |
| 3 Tonleitern | 8 Ganz- und Halbtöne, Dur-Tonleiter | Halbton, Ganzton, Bauplan Dur, Dur-Tonleitern bilden, Tonart, Tetrachorde | Klasse 8 |
| | 9 Moll-Tonleitern | natürliches, harmonisches, melodisches Moll, Paralleltonarten | Klasse 8 |
| 4 Intervalle und Dreiklänge | 10 Intervalle | Prime bis Oktave, rein/groß/klein, bestimmen und notieren | Klasse 9 |
| | 11 Dreiklänge | Terzschichtung, Dur/Moll/vermindert/übermäßig, Akkordsymbole, Hauptdreiklänge, Umkehrungen | Klasse 8 |
| 5 Quintenzirkel | 12 Der Quintenzirkel | Herleitung über Tetrachorde, Kreuz- und b-Tonarten, Reihenfolge der Vorzeichen, Tonart bestimmen, Abschlusstest | Klasse 10 |

Die Intervalle stehen vor den Dreiklängen, weil die Terzschichtung große und kleine Terzen voraussetzt.

Zu jedem Kapitel gibt es

- einen **Lerntext** mit Notenbeispielen zum Anhören,
- **Aufgaben** als druckbares Arbeitsblatt (AFB I bis III, mit Notenzeilen),
- **Übungen** mit sofortiger Rückmeldung: Notenquiz, Noten lesen, Noten per Klick notieren, Halbtöne markieren, Zuordnen, Sortieren, Reihenfolge.

Dazu kommen vier **Werkzeuge**: Klaviatur, interaktiver Quintenzirkel, Taktbaukasten und Notentrainer (Zufallsaufgaben).

„Prüfen“ und „Lösung zeigen“ werden erst freigegeben, wenn eine Übung vollständig bearbeitet ist. Beim Quiz gibt es die Rückmeldung direkt nach jeder beantworteten Frage.

## Kapitel und Stufen freischalten (für Lehrkräfte)

Die Einstellungen stehen in der Datei [`freigabe.json`](freigabe.json). Ändern: Datei auf GitHub öffnen, auf den Stift („Edit this file“) klicken, `true` oder `false` eintragen, „Commit changes“ klicken. Nach etwa zwei Minuten ist die Website aktualisiert (Reiter „Actions“).

- **„Kapitel 1“ bis „Kapitel 12“:** `false` sperrt ein Kapitel ganz. Es wird dann gar nicht als Seite veröffentlicht.
- **„Stufen nacheinander freischalten“:** Bei `true` sehen Schülerinnen und Schüler zunächst nur Stufe 1. Die nächste Stufe öffnet sich, sobald alle Übungen der vorherigen Stufe mit mindestens 80 Prozent gelöst sind. Bei `false` sind alle freigeschalteten Kapitel sofort zugänglich, zum Beispiel für die eigene Vorbereitung oder wenn die Klasse gezielt einzelne Themen wiederholen soll.

Wichtig zur stufenweisen Freischaltung:

- **Codes:** Unter „Codes“ steht für jede Stufe ab Stufe 2 ein vierstelliger Code. Wer ihn bei einer gesperrten Stufe eingibt, schaltet diese Stufe (und alle davor) auf dem jeweiligen Gerät sofort frei, ohne die Übungen zu lösen. Die nächste Stufe öffnet sich dann wieder über die Übungen oder ihren eigenen Code. Codes ändern: in `freigabe.json` neue vier Ziffern eintragen und speichern. Auf der Website steht nur eine Prüfsumme, nicht der Code selbst; im öffentlichen Repository ist `freigabe.json` aber lesbar.
- **Fortschrittscode:** Auf der Startseite können Schülerinnen und Schüler ihren Fortschritt (gelöste Übungen ab 80 % und per Code freigeschaltete Stufen) als kurzen Code anzeigen lassen und auf einem anderen Gerät wieder eingeben. Dabei wird nichts übertragen, der Code enthält die Daten selbst. Die Reihenfolge der Übungen im Code steht in `werkzeug/code_reihenfolge.json`. Neue Übungen werden dort automatisch hinten angehängt. Die Datei bitte nicht umsortieren, sonst passen alte Codes nicht mehr.
- Der Fortschritt wird nur im Browser des jeweiligen Geräts gespeichert (localStorage). Es wird nichts übertragen, und es gibt keine Anmeldung. Auf einem anderen Gerät oder nach dem Löschen der Browserdaten beginnt man wieder bei Stufe 1. Auf der Startseite gibt es einen Knopf zum Zurücksetzen.
- Erlaubt ein Browser keine Speicherung (z. B. bestimmte private Fenster), sind alle Stufen offen.
- Die Sperre ist eine Lernhilfe, kein Schutz: Technisch versierte Schülerinnen und Schüler können sie umgehen. Wirklich verbergen lassen sich Inhalte nur über die Kapitel-Schalter.
- Die Arbeitsblätter zählen nicht für die Freischaltung, nur die interaktiven Übungen. Die Werkzeuge sind immer offen.

Hinweis: Weil das Repository öffentlich ist, bleiben die Quelltexte im Ordner `werkzeug/` auf GitHub einsehbar.

## Seiten neu erzeugen

Alle HTML-Seiten entstehen aus den Python-Dateien in `werkzeug/` (Inhalte in `kap_*.py`). Für den Notensatz wird Node.js benötigt. Aufruf: `cd werkzeug && python3 bauen.py`.

## Datenschutz und Urheberrecht

- Keine externen Inhalte, keine Datenübertragung, keine Anmeldung. Nur der Lernfortschritt wird lokal im Browser gespeichert. Der Klang wird im Browser erzeugt (Web Audio).
- Texte, Aufgaben, Zeichnungen und Programmcode sind eigens erstellt. Die Notenbeispiele sind eigene Beispiele oder gemeinfreie Tonfolgen; Liedtitel werden nur als Hörhilfe genannt.
- Notenzeichen: Schrift Bravura (Steinberg) unter der SIL Open Font License (`assets/OFL-Bravura.txt`). Schriften Atkinson Hyperlegible, Bricolage Grotesque und Caveat ebenfalls unter der SIL Open Font License (`assets/fonts/`).
