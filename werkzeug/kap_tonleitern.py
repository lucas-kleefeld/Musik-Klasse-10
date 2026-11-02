"""Kapitel 7 und 8: Ganz- und Halbtöne, Dur- und Moll-Tonleitern."""
from notensatz import N
from kap_tonhoehe import klaviatur_bild
import theorie as T


def leiter(toene, boegen=True, labels=None, hl=()):
    teile = []
    for i, t in enumerate(toene):
        if i and boegen:
            d = T.midi(t) - T.midi(toene[i - 1])
            teile.append("{HT}" if d == 1 else "{GT}" if d == 2 else "{1½}")
        lab = ("@" + labels[i]) if labels else ""
        teile.append(("*" if i in hl else "") + f"{t}/1{lab}")
    return " ".join(teile)


def stufen_labels(n=8):
    return [str(i + 1) for i in range(n)]


def leiter_aufgabe(grundton, schritte, name):
    toene = T.tonleiter(grundton, schritte)
    return {"frage": f"Notiere die {name}-Tonleiter aufwärts. Der Grundton ist vorgegeben.", "vorgabe": [toene[0]], "ziel": toene[1:], "folge": True}


def halbton_aufgabe(grundton, schritte, frage):
    toene = T.tonleiter(grundton, schritte)
    gaps = [i for i in range(7) if T.midi(toene[i + 1]) - T.midi(toene[i]) == 1]
    return {"frage": frage, "noten": " ".join(f"{t}/1" for t in toene), "loesung": gaps}


KAPITEL = {}

# ======================================================================
KAPITEL[7] = {
"kurz": "Halbtöne und Ganztöne, der Bauplan der Dur-Tonleiter und wie man Dur-Tonleitern auf jedem Ton bildet.",
"inhalt": f"""
<p class="lead">Spielt man auf dem Klavier nur die weißen Tasten von c bis c, klingt es nach „Do-Re-Mi“. Warum das so ist, verrät ein Blick auf die Abstände zwischen den Tönen.</p>

<h2>Halbton und Ganzton</h2>
<ul>
  <li>Ein <span class="fachwort">Halbton</span> ist der kleinste Abstand: von einer Taste zur <strong>direkt benachbarten</strong> Taste, egal ob weiß oder schwarz.</li>
  <li>Ein <span class="fachwort">Ganzton</span> besteht aus <strong>zwei Halbtönen</strong>: Dazwischen liegt genau eine Taste.</li>
</ul>
<p>Zwischen den weißen Tasten e–f und h–c liegt keine schwarze Taste. Diese beiden Stammton-Schritte sind deshalb <strong>natürliche Halbtöne</strong>. Alle anderen benachbarten Stammtöne sind Ganztöne voneinander entfernt.</p>
<figure class="breit klavier"><div class="bild">{klaviatur_bild(0, 8, "stamm", (2, 3, 6, 7), "Klaviatur mit den natürlichen Halbtönen", "Eine Oktave von c bis c. Die Tasten e, f, h und c sind markiert, weil zwischen e und f sowie h und c keine schwarze Taste liegt.")}</div><figcaption>e–f und h–c: Halbtöne ohne schwarze Taste dazwischen</figcaption></figure>

<h2>Der Bauplan der Dur-Tonleiter</h2>
<p>Eine <span class="fachwort">Tonleiter</span> ist eine Folge von acht Tönen vom <strong>Grundton</strong> bis zu seiner Oktave. Die Töne heißen <strong>Stufen</strong> und werden von 1 bis 8 gezählt. Bei jeder <span class="fachwort">Dur-Tonleiter</span> liegen die Halbtöne an denselben Stellen: <strong>zwischen der 3. und 4. sowie der 7. und 8. Stufe</strong>.</p>
{N(leiter(T.tonleiter("C4"), labels=stufen_labels()), "C-Dur: Ganzton – Ganzton – Halbton – Ganzton – Ganzton – Ganzton – Halbton", zoom=1.6)}
<div class="formel">1 – 1 – ½ – 1 – 1 – 1 – ½</div>
<p>Die C-Dur-Tonleiter kommt ohne Vorzeichen aus, weil die natürlichen Halbtöne e–f und h–c genau an den richtigen Stellen liegen.</p>

<h2>Dur-Tonleitern auf anderen Tönen</h2>
<p>Beginnt man auf einem anderen Grundton, passen die natürlichen Halbtöne nicht mehr. Dann braucht man Vorzeichen, damit der Bauplan stimmt.</p>
<ol>
  <li>Grundton notieren und die Stammtöne bis zur Oktave aufschreiben.</li>
  <li>Die Abstände bestimmen (Klaviatur hilft).</li>
  <li>Wo der Bauplan nicht stimmt, einen Ton mit ♯ erhöhen oder mit ♭ erniedrigen.</li>
</ol>
{N(leiter(T.tonleiter("G4"), labels=stufen_labels(), hl=(6,)), "G-Dur: Ohne Vorzeichen wäre zwischen e und f ein Halbton an der falschen Stelle. Mit fis stimmt der Bauplan.", zoom=1.6)}
{N(leiter(T.tonleiter("F4"), labels=stufen_labels(), hl=(3,)), "F-Dur: Aus h wird b, damit zwischen der 3. und 4. Stufe ein Halbton liegt.", zoom=1.6)}
{N(leiter(T.tonleiter("D4"), labels=stufen_labels(), hl=(2, 6)), "D-Dur braucht zwei Kreuze: fis und cis.", zoom=1.6)}
<p>In einer Tonleiter kommt jeder Stammbuchstabe genau einmal vor. Deshalb heißt der 4. Ton in F-Dur <strong>b</strong> und nicht ais.</p>

<h2>Tonart</h2>
<p>Steht ein Musikstück in einer bestimmten Dur-Tonleiter, sagt man, es steht in dieser <span class="fachwort">Tonart</span>, zum Beispiel in G-Dur. Die nötigen Vorzeichen schreibt man dann als Generalvorzeichen an den Zeilenanfang. Der Grundton heißt auch <strong>Tonika</strong>: Mit ihm enden die meisten Stücke, er wirkt wie „zu Hause“.</p>
{N("G4/4 A4/4 B4/4 C5/4 | D5/4 E5/4 F5/4 G5/4 |.", "G-Dur mit Generalvorzeichen: Das fis gilt für jedes f.", tonart=1, takt="4/4", zoom=1.6)}
<p>Übrigens: Eine Dur-Tonleiter besteht aus zwei gleich gebauten Hälften (1 – 1 – ½), die durch einen Ganzton verbunden sind. Diese Hälften heißen <strong>Tetrachorde</strong>. Sie spielen beim Quintenzirkel (Kapitel 11) eine Rolle.</p>
<p><a class="knopf leise" href="../werkzeuge/klaviatur.html">Tonleitern auf der Klaviatur spielen</a></p>

<div class="merke"><strong>Merke</strong>
<p>Halbton = benachbarte Tasten, Ganzton = zwei Halbtöne. Natürliche Halbtöne liegen zwischen e–f und h–c. Jede Dur-Tonleiter hat den Bauplan 1 – 1 – ½ – 1 – 1 – 1 – ½: Halbtöne zwischen der 3./4. und 7./8. Stufe. Auf anderen Grundtönen sorgen Vorzeichen dafür, dass der Bauplan stimmt.</p></div>
""",
"aufgaben": [
 ("I", "Erkläre die Begriffe Halbton und Ganzton mithilfe der Klaviatur.", 3, ""),
 ("I", "Markiere in der C-Dur-Tonleiter die Halbtonschritte mit einem Bogen und beschrifte die Stufen.", 0, N(" ".join(f"{t}/1" for t in T.tonleiter("C4")), zoom=1.5)),
 ("II", "Bestimme, ob zwischen den Tönen ein Ganzton oder ein Halbton liegt: e–f, f–g, h–c, a–b, cis–d, fis–gis.", 3, ""),
 ("II", "Notiere die Tonleitern G-Dur, F-Dur und D-Dur. Markiere die Halbtöne.", 0, N("", breite=520) + N("", breite=520) + N("", breite=520)),
 ("II", "Bilde die A-Dur-Tonleiter. Erkläre Schritt für Schritt, welche Vorzeichen nötig sind.", 6, ""),
 ("III", "Ein Mitschüler notiert die F-Dur-Tonleiter so: f g a ais c d e f. Erkläre, was daran falsch ist.", 4, ""),
],
"uebungen": [
 {"slug": "k7-halbtoene", "titel": "Halbtöne finden", "kurz": "Die Halbtonschritte in Dur-Tonleitern markieren", "typ": "halbtoene", "symbol": "halbtoene",
  "anleitung": "Tippe zwischen zwei Noten, um dort einen Halbton zu markieren. Markiere in jeder Tonleiter genau zwei Halbtöne.",
  "daten": {"aufgaben": [halbton_aufgabe(g, T.DUR, f"{n}-Dur: Wo liegen die Halbtöne?") for g, n in [("C4", "C"), ("G4", "G"), ("F4", "F"), ("D4", "D"), ("Bb3", "B"), ("A4", "A")]]}},
 {"slug": "k7-tonleiter-notieren", "titel": "Dur-Tonleitern notieren", "kurz": "Tonleitern mit den richtigen Vorzeichen setzen", "typ": "notieren", "symbol": "notieren",
  "anleitung": "Setze die Töne der Tonleiter nacheinander. Wähle bei Bedarf vorher ♯ oder ♭.",
  "daten": {"vorzeichen": True, "aufgaben": [leiter_aufgabe(g, T.DUR, n) for g, n in [("C4", "C-Dur"), ("G4", "G-Dur"), ("F4", "F-Dur"), ("D4", "D-Dur")]]}},
 {"slug": "k7-quiz", "titel": "Quiz: Ganzton, Halbton, Dur", "kurz": "Abstände bestimmen und Dur-Tonleitern erkennen", "typ": "notenquiz", "symbol": "quiz",
  "anleitung": "Wähle die richtige Antwort.",
  "daten": {"fragen": [
   {"frage": "Welcher Abstand liegt zwischen diesen Tönen?", "noten": "E4/1 F4/1", "optionen": ["Halbton", "Ganzton"], "richtig": 0, "erklaerung": "e–f ist ein natürlicher Halbton."},
   {"frage": "Welcher Abstand liegt zwischen diesen Tönen?", "noten": "F4/1 G4/1", "optionen": ["Ganzton", "Halbton"], "richtig": 0, "erklaerung": "Dazwischen liegt fis."},
   {"frage": "Welcher Abstand liegt zwischen diesen Tönen?", "noten": "A4/1 Bb4/1", "optionen": ["Halbton", "Ganzton"], "richtig": 0, "erklaerung": "a und b sind benachbarte Tasten."},
   {"frage": "Welcher Abstand liegt zwischen diesen Tönen?", "noten": "C#5/1 D#5/1", "optionen": ["Ganzton", "Halbton"], "richtig": 0, "erklaerung": "Dazwischen liegt d."},
   {"frage": "Zwischen welchen Stufen liegen in Dur die Halbtöne?", "optionen": ["3–4 und 7–8", "2–3 und 5–6", "4–5 und 7–8", "1–2 und 5–6"], "richtig": 0, "erklaerung": "Bauplan 1 – 1 – ½ – 1 – 1 – 1 – ½."},
   {"frage": "Welche Tonleiter ist eine richtige Dur-Tonleiter?", "optionen": [{"noten": " ".join(f"{t}/1" for t in T.tonleiter("G4")), "spec": {}}, {"noten": "G4/1 A4/1 B4/1 C5/1 D5/1 E5/1 F5/1 G5/1", "spec": {}}, {"noten": "G4/1 A4/1 Bb4/1 C5/1 D5/1 E5/1 F#5/1 G5/1", "spec": {}}], "richtig": 0, "erklaerung": "G-Dur braucht fis, sonst liegt der Halbton e–f an der falschen Stelle."},
   {"frage": "Welches Vorzeichen braucht F-Dur?", "optionen": ["b", "fis", "es", "keins"], "richtig": 0, "erklaerung": "Zwischen a und b liegt der Halbton der 3./4. Stufe."},
   {"frage": "Welche Vorzeichen braucht D-Dur?", "optionen": ["fis und cis", "nur fis", "b und es", "fis, cis und gis"], "richtig": 0, "erklaerung": "d e fis g a h cis d."},
   {"frage": "Welcher Ton ist in A-Dur die 3. Stufe?", "optionen": ["cis", "c", "d", "h"], "richtig": 0, "erklaerung": "a h cis d e fis gis a."},
   {"frage": "Warum heißt der 4. Ton von F-Dur „b“ und nicht „ais“?", "optionen": ["Jeder Stammbuchstabe kommt in einer Tonleiter genau einmal vor.", "Weil ais höher klingt.", "Weil es kein ais gibt.", "Weil F-Dur nur Kreuze hat."], "richtig": 0, "erklaerung": "Nach a muss ein h-Ton folgen, also h oder b."}
  ]}},
],
}

# ======================================================================
KAPITEL[8] = {
"kurz": "Der Bauplan der natürlichen Moll-Tonleiter, Paralleltonarten sowie harmonisches und melodisches Moll.",
"inhalt": f"""
<p class="lead">Spielt man nur die weißen Tasten, aber von a bis a, klingt die Tonleiter auf einmal ganz anders: eher dunkel, ernst oder traurig. Das ist <span class="fachwort">Moll</span>.</p>

<h2>Der Bauplan der natürlichen Moll-Tonleiter</h2>
{N(leiter(T.tonleiter("A4", T.MOLL), labels=stufen_labels()), "a-Moll: Ganzton – Halbton – Ganzton – Ganzton – Halbton – Ganzton – Ganzton", zoom=1.6)}
<div class="formel">1 – ½ – 1 – 1 – ½ – 1 – 1</div>
<p>In der <span class="fachwort">natürlichen Moll-Tonleiter</span> liegen die Halbtöne <strong>zwischen der 2. und 3. sowie der 5. und 6. Stufe</strong>. Der wichtigste Unterschied zu Dur: Der Abstand vom Grundton zur 3. Stufe ist kleiner. Diese <strong>kleine Terz</strong> (drei Halbtöne) gibt Moll seinen typischen Klang.</p>
{N(leiter(T.tonleiter("C4"), boegen=False, hl=(2,)) + " || " + leiter(T.tonleiter("C4", T.MOLL), boegen=False, hl=(2, 5, 6)), "C-Dur und c-Moll im Vergleich: In c-Moll sind die 3., 6. und 7. Stufe einen Halbton tiefer.", zoom=1.5)}
<p>Tonarten mit demselben Grundton, wie C-Dur und c-Moll, heißen <strong>gleichnamige Tonarten</strong>. Übrigens: Dur-Tonarten schreibt man mit großem Anfangsbuchstaben, Moll-Tonarten mit kleinem.</p>

<h2>Paralleltonarten</h2>
<p>a-Moll hat dieselben Töne wie C-Dur, also auch dieselben Vorzeichen (keine). Solche Tonart-Paare heißen <span class="fachwort">Paralleltonarten</span>. Den Grundton der parallelen Moll-Tonart findet man so:</p>
<ul>
  <li>Von der Dur-Tonika aus <strong>drei Halbtöne (eine kleine Terz) abwärts</strong> gehen: C → a, G → e, F → d.</li>
  <li>Oder: Die <strong>6. Stufe</strong> der Dur-Tonleiter ist der Grundton der parallelen Moll-Tonleiter.</li>
</ul>
<div class="tabelle-scroll"><table>
  <thead><tr><th>Dur</th><th>parallele Moll-Tonart</th><th>Vorzeichen</th></tr></thead>
  <tbody>
    <tr><td>C-Dur</td><td>a-Moll</td><td>keine</td></tr>
    <tr><td>G-Dur</td><td>e-Moll</td><td>fis</td></tr>
    <tr><td>D-Dur</td><td>h-Moll</td><td>fis, cis</td></tr>
    <tr><td>F-Dur</td><td>d-Moll</td><td>b</td></tr>
    <tr><td>B-Dur</td><td>g-Moll</td><td>b, es</td></tr>
  </tbody>
</table></div>
{N(leiter(T.tonleiter("E4", T.MOLL), labels=stufen_labels()), "e-Moll hat wie G-Dur ein fis.", zoom=1.6)}

<h2>Harmonisches und melodisches Moll</h2>
<p>In der natürlichen Moll-Tonleiter liegt zwischen der 7. und 8. Stufe ein Ganzton. Die Melodie „strebt“ dadurch weniger stark zum Grundton. Deshalb verändert man die Tonleiter oft:</p>
<ul>
  <li><strong>Harmonisches Moll:</strong> Die 7. Stufe wird um einen Halbton erhöht. Zwischen 6. und 7. Stufe entsteht ein großer Schritt von drei Halbtönen (1½). Der erhöhte 7. Ton heißt <strong>Leitton</strong>, weil er zum Grundton hinleitet.</li>
  <li><strong>Melodisches Moll:</strong> Aufwärts werden die 6. und 7. Stufe erhöht, abwärts gilt die natürliche Form.</li>
</ul>
{N(leiter(T.tonleiter("A4", T.MOLL_HARM), labels=stufen_labels(), hl=(6,)), "a-Moll harmonisch: gis als Leitton", zoom=1.6)}
{N(leiter(T.tonleiter("A4", [2, 1, 2, 2, 2, 2, 1]), labels=stufen_labels(), hl=(5, 6)), "a-Moll melodisch (aufwärts): fis und gis", zoom=1.6)}

<div class="merke"><strong>Merke</strong>
<p>Natürliches Moll hat den Bauplan 1 – ½ – 1 – 1 – ½ – 1 – 1 mit Halbtönen zwischen 2./3. und 5./6. Stufe. Jede Dur-Tonart hat eine parallele Moll-Tonart mit denselben Vorzeichen. Ihr Grundton liegt eine kleine Terz (drei Halbtöne) unter dem Dur-Grundton. Im harmonischen Moll ist die 7. Stufe erhöht (Leitton).</p></div>
""",
"aufgaben": [
 ("I", "Notiere die a-Moll-Tonleiter und markiere die Halbtöne.", 0, N("", breite=520)),
 ("I", "Nenne die parallele Moll-Tonart zu C-Dur, G-Dur, F-Dur und D-Dur.", 2, ""),
 ("II", "Vergleiche die Baupläne von Dur und natürlichem Moll. Beschreibe die Unterschiede.", 4, ""),
 ("II", "Notiere e-Moll natürlich und e-Moll harmonisch. Markiere den Unterschied.", 0, N("", breite=520) + N("", breite=520)),
 ("II", "Bestimme, ob es sich um eine Dur- oder Moll-Tonleiter handelt, und begründe.", 4, N(" ".join(f"{t}/1" for t in T.tonleiter("D4", T.MOLL)), zoom=1.4)),
 ("III", "Hört euch ein bekanntes Lied in Dur an und singt oder spielt es danach in Moll (3. Stufe tiefer). Beschreibt, wie sich die Wirkung verändert.", 0, ""),
],
"uebungen": [
 {"slug": "k8-halbtoene", "titel": "Halbtöne in Moll finden", "kurz": "Halbtonschritte in Moll-Tonleitern markieren", "typ": "halbtoene", "symbol": "halbtoene",
  "anleitung": "Tippe zwischen zwei Noten, um dort einen Halbton zu markieren. Markiere in jeder Tonleiter genau zwei Halbtöne.",
  "daten": {"aufgaben": [halbton_aufgabe(g, T.MOLL, f"{n}-Moll (natürlich): Wo liegen die Halbtöne?") for g, n in [("A4", "a"), ("E4", "e"), ("D4", "d"), ("G4", "g")]]}},
 {"slug": "k8-notieren", "titel": "Moll-Tonleitern notieren", "kurz": "Natürliche und harmonische Moll-Tonleitern setzen", "typ": "notieren", "symbol": "notieren",
  "anleitung": "Setze die Töne der Tonleiter nacheinander. Wähle bei Bedarf vorher ♯ oder ♭.",
  "daten": {"vorzeichen": True, "aufgaben": [leiter_aufgabe("A4", T.MOLL, "a-Moll (natürlich)"), leiter_aufgabe("E4", T.MOLL, "e-Moll (natürlich)"), leiter_aufgabe("D4", T.MOLL, "d-Moll (natürlich)"), leiter_aufgabe("A4", T.MOLL_HARM, "a-Moll (harmonisch)")]}},
 {"slug": "k8-parallel", "titel": "Zuordnen: Paralleltonarten", "kurz": "Dur-Tonarten und ihre parallelen Moll-Tonarten", "typ": "zuordnen", "symbol": "zuordnen",
  "anleitung": "Wähle zu jeder Dur-Tonart die parallele Moll-Tonart.",
  "daten": {"paare": [{"links": T.TONARTEN[k][0], "rechts": T.TONARTEN[k][1]} for k in (0, 1, 2, 3, -1, -2, -3)]}},
 {"slug": "k8-quiz", "titel": "Quiz: Dur oder Moll?", "kurz": "Tonleitern erkennen und Moll-Formen unterscheiden", "typ": "notenquiz", "symbol": "quiz",
  "anleitung": "Wähle die richtige Antwort.",
  "daten": {"fragen": [
   {"frage": "Ist das eine Dur- oder eine Moll-Tonleiter?", "noten": " ".join(f"{t}/1" for t in T.tonleiter("E4", T.MOLL)), "optionen": ["Moll (e-Moll)", "Dur (E-Dur)"], "richtig": 0, "erklaerung": "Halbtöne zwischen 2./3. und 5./6. Stufe."},
   {"frage": "Ist das eine Dur- oder eine Moll-Tonleiter?", "noten": " ".join(f"{t}/1" for t in T.tonleiter("D4")), "optionen": ["Dur (D-Dur)", "Moll (d-Moll)"], "richtig": 0, "erklaerung": "Halbtöne zwischen 3./4. und 7./8. Stufe."},
   {"frage": "Welche Moll-Form ist das?", "noten": " ".join(f"{t}/1" for t in T.tonleiter("A4", T.MOLL_HARM)), "optionen": ["harmonisches Moll", "natürliches Moll", "melodisches Moll", "Dur"], "richtig": 0, "erklaerung": "Nur die 7. Stufe (gis) ist erhöht."},
   {"frage": "Was ist die parallele Moll-Tonart von F-Dur?", "optionen": ["d-Moll", "f-Moll", "a-Moll", "g-Moll"], "richtig": 0, "erklaerung": "Drei Halbtöne unter f liegt d."},
   {"frage": "Was ist die parallele Dur-Tonart von e-Moll?", "optionen": ["G-Dur", "E-Dur", "C-Dur", "A-Dur"], "richtig": 0, "erklaerung": "Drei Halbtöne über e liegt g."},
   {"frage": "Zwischen welchen Stufen liegen im natürlichen Moll die Halbtöne?", "optionen": ["2–3 und 5–6", "3–4 und 7–8", "2–3 und 7–8", "4–5 und 6–7"], "richtig": 0, "erklaerung": "1 – ½ – 1 – 1 – ½ – 1 – 1."},
   {"frage": "Welche Stufe macht den Hauptunterschied zwischen C-Dur und c-Moll aus?", "optionen": ["die 3. Stufe (e oder es)", "die 1. Stufe", "die 5. Stufe", "die 8. Stufe"], "richtig": 0, "erklaerung": "Große Terz in Dur, kleine Terz in Moll."},
   {"frage": "Wie heißt der erhöhte 7. Ton im harmonischen Moll?", "optionen": ["Leitton", "Grundton", "Tonika", "Halbton"], "richtig": 0, "erklaerung": "Er leitet zum Grundton."}
  ]}},
],
}
