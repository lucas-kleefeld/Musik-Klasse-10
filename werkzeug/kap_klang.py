"""Kapitel 9 und 10: Intervalle und Dreiklänge."""
import random
from notensatz import N
import theorie as T

INT_NAMEN = ["reine Prime", "kleine Sekunde", "große Sekunde", "kleine Terz", "große Terz", "reine Quarte", "übermäßige Quarte",
             "reine Quinte", "kleine Sexte", "große Sexte", "kleine Septime", "große Septime", "reine Oktave"]


def harm(a, b, dauer="1", label=""):
    lab = ("@" + label.replace(" ", "_")) if label else ""
    return f"[{a} {b}]/{dauer}{lab}"


def int_frage(a, b):
    richtig = T.intervall(a, b)
    random.seed(a + b)
    falsche = [n for n in INT_NAMEN if n != richtig]
    # plausible falsche Antworten: gleiche Stufenzahl zuerst
    grund = richtig.split()[-1]
    nah = [n for n in falsche if n.split()[-1] == grund]
    rest = random.sample([n for n in falsche if n not in nah], 3 - min(3, len(nah)))
    opt = [richtig] + (nah + rest)[:3]
    return {"frage": "Welches Intervall ist das?", "noten": harm(a, b), "optionen": opt, "richtig": 0,
            "erklaerung": f"{T.name(a)} – {T.name(b)}: {T.stufe(b) - T.stufe(a) + 1} Stufen, {T.midi(b) - T.midi(a)} Halbtöne."}


INT_BEISPIELE = [("C4", "C4"), ("C4", "Db4"), ("C4", "D4"), ("C4", "Eb4"), ("C4", "E4"), ("C4", "F4"), ("C4", "F#4"), ("C4", "G4"), ("C4", "Ab4"), ("C4", "A4"), ("C4", "Bb4"), ("C4", "B4"), ("C4", "C5")]

KAPITEL = {}

# ======================================================================
KAPITEL[9] = {
"kurz": "Namen der Intervalle von der Prime bis zur Oktave, reine, große und kleine Intervalle, Intervalle bestimmen und notieren.",
"inhalt": f"""
<p class="lead">Der Abstand zwischen zwei Tönen heißt <span class="fachwort">Intervall</span>. Intervalle bestimmen, wie eine Melodie klingt und wie Akkorde gebaut sind.</p>

<h2>Melodisch oder harmonisch</h2>
<p>Erklingen die beiden Töne nacheinander, spricht man von einem <strong>melodischen</strong> Intervall. Erklingen sie gleichzeitig, ist es ein <strong>harmonisches</strong> Intervall.</p>
{N("C4/2 G4/2 | [C4 G4]/1 |", "Die Quinte c′–g′ melodisch und harmonisch", takt="4/4", zoom=1.6)}

<h2>Die Namen: Stufen zählen</h2>
<p>Die Namen kommen aus dem Lateinischen und geben an, die wievielte Stufe der obere Ton ist. Dabei zählt man den <strong>unteren Ton als 1</strong> mit.</p>
{N(" ".join(harm("C4", t, "1", n) for t, n in [("C4", "Prime"), ("D4", "Sekunde"), ("E4", "Terz"), ("F4", "Quarte"), ("G4", "Quinte"), ("A4", "Sexte"), ("B4", "Septime"), ("C5", "Oktave")]),
   "1 Prime, 2 Sekunde, 3 Terz, 4 Quarte, 5 Quinte, 6 Sexte, 7 Septime, 8 Oktave", zoom=1.6)}
<p>Ein Trick im Notenbild: Bei <strong>ungeraden</strong> Intervallen (Prime, Terz, Quinte, Septime) liegen beide Noten auf Linien oder beide in Zwischenräumen. Bei <strong>geraden</strong> (Sekunde, Quarte, Sexte, Oktave) liegt eine Note auf einer Linie, die andere in einem Zwischenraum.</p>

<h2>Rein, groß und klein: Halbtöne zählen</h2>
<p>Die Stufenzahl allein reicht nicht: c–e und c–es sind beide Terzen, klingen aber verschieden. Deshalb zählt man zusätzlich die <strong>Halbtöne</strong>.</p>
<ul>
  <li>Prime, Quarte, Quinte und Oktave heißen <strong>rein</strong>.</li>
  <li>Sekunde, Terz, Sexte und Septime gibt es <strong>groß</strong> und <strong>klein</strong>. Das kleine Intervall ist einen Halbton kleiner als das große.</li>
</ul>
<div class="tabelle-scroll"><table>
  <thead><tr><th>Intervall</th><th>Halbtöne</th><th>Beispiel ab c′</th></tr></thead>
  <tbody>
""" + "".join(f"<tr><td>{T.intervall(a, b)}</td><td>{T.midi(b) - T.midi(a)}</td><td>{T.name(a)}′ – {T.name(b, True)}</td></tr>" for a, b in INT_BEISPIELE) + f"""
  </tbody>
</table></div>
<p>Die übermäßige Quarte (zum Beispiel f–h) teilt die Oktave genau in zwei Hälften und klingt sehr spannungsreich. Sie heißt auch <strong>Tritonus</strong>, weil sie aus drei Ganztönen besteht.</p>

<h2>Ein Intervall bestimmen</h2>
<ol>
  <li><strong>Stufen zählen</strong> (unteren Ton als 1 mitzählen): Das ergibt den Grundnamen, z. B. Terz.</li>
  <li><strong>Halbtöne zählen</strong> (auf der Klaviatur oder im Kopf): Das ergibt rein, groß oder klein.</li>
</ol>
{N(harm("E4", "G4", "1", "kleine Terz") + " " + harm("D4", "A4", "1", "reine Quinte") + " " + harm("F4", "D5", "1", "große Sexte") + " " + harm("A4", "G5", "1", "kleine Septime"), "Beispiele: e′–g′ (3 Halbtöne), d′–a′ (7), f′–d″ (9), a′–g″ (10)", zoom=1.6)}
<p>Vorzeichen ändern nicht die Stufenzahl, nur die Halbtonzahl: c–e ist eine große Terz, c–es eine kleine Terz, cis–e wieder eine kleine Terz.</p>
<p>Noch ein Trick: Ist der untere Ton der Grundton einer Dur-Tonleiter, dann sind alle Töne dieser Tonleiter darüber <strong>große oder reine</strong> Intervalle.</p>

<h2>Ein Intervall notieren</h2>
<p>Beispiel: eine kleine Sexte über e′.</p>
<ol>
  <li>Sechs Stufen zählen: e – f – g – a – h – <strong>c</strong>. Der Ton ist also ein c″ (mit oder ohne Vorzeichen).</li>
  <li>Halbtöne prüfen: e′–c″ hat 8 Halbtöne. Die kleine Sexte braucht 8. Es passt, kein Vorzeichen nötig.</li>
</ol>

<h2>Intervalle hören</h2>
<p>Viele bekannte Melodien beginnen mit einem typischen Intervall. Das hilft beim Erkennen:</p>
<ul>
  <li>große Sekunde: „Alle meine Entchen“</li>
  <li>kleine Terz: „Kuckuck, Kuckuck, ruft’s aus dem Wald“</li>
  <li>reine Quarte: „O Tannenbaum“</li>
  <li>reine Quinte: „Morgen kommt der Weihnachtsmann“</li>
  <li>reine Oktave: „Somewhere over the Rainbow“</li>
</ul>
<p><a class="knopf leise" href="../werkzeuge/klaviatur.html">Intervalle auf der Klaviatur anhören</a> <a class="knopf leise" href="../werkzeuge/notentrainer.html">Intervalle trainieren</a></p>

<div class="merke"><strong>Merke</strong>
<p>Ein Intervall ist der Abstand zweier Töne. Den Namen bestimmt man in zwei Schritten: Stufen zählen (Prime bis Oktave) und Halbtöne zählen. Prime, Quarte, Quinte und Oktave sind rein; Sekunde, Terz, Sexte und Septime sind groß oder klein. Kleine Terz = 3, große Terz = 4, reine Quinte = 7 Halbtöne.</p></div>
""",
"aufgaben": [
 ("I", "Nenne die Intervallnamen von der Prime bis zur Oktave.", 2, ""),
 ("I", "Bestimme die Intervalle (Stufen und Halbtöne).", 0, N(" ".join(harm(a, b) for a, b in [("D4", "F4"), ("E4", "B4"), ("G4", "E5"), ("C4", "F4"), ("A4", "C5"), ("F4", "E5"), ("B4", "D5"), ("D4", "D5")]), zoom=1.5)),
 ("II", "Notiere jeweils über dem Ton: große Terz über d′, reine Quinte über f′, kleine Sexte über a′, große Sekunde über e′, reine Quarte über b′, kleine Septime über g′.", 0, N("D4/1 _ F4/1 _ A4/1 _ E4/1 _ Bb4/1 _ G4/1", zoom=1.5)),
 ("II", "Erkläre, warum c′–e′ und c′–es′ zwar beide Terzen sind, aber unterschiedlich heißen.", 3, ""),
 ("II", "Bestimme die melodischen Intervalle zwischen den Tönen dieses Liedanfangs.", 0, N("C4/4 C4/4 G4/4 G4/4 | A4/4 A4/4 G4/2 | F4/4 F4/4 E4/4 E4/4 | D4/4 D4/4 C4/2 |.", takt="4/4", zoom=1.4)),
 ("III", "Erkläre, warum man beim Bestimmen eines Intervalls immer erst die Stufen und dann die Halbtöne zählen sollte. Was passiert, wenn man nur Halbtöne zählt?", 5, ""),
],
"uebungen": [
 {"slug": "k9-bestimmen", "titel": "Intervalle bestimmen", "kurz": "Stufen und Halbtöne zählen und das Intervall benennen", "typ": "notenquiz", "symbol": "intervalle",
  "anleitung": "Bestimme das Intervall. Mit „Anhören“ kannst du es dir vorspielen lassen.",
  "daten": {"hoeren": True, "fragen": [int_frage(a, b) for a, b in [("C4", "E4"), ("D4", "F4"), ("E4", "B4"), ("F4", "C5"), ("G4", "E5"), ("A4", "C5"), ("C4", "A4"), ("E4", "C5"),
                                                                   ("D4", "C5"), ("C4", "B4"), ("F4", "B4"), ("G4", "G5"), ("Bb4", "D5"), ("D4", "F#4"), ("E4", "G#4"), ("Eb4", "Bb4")]]}},
 {"slug": "k9-notieren", "titel": "Intervalle notieren", "kurz": "Den oberen Ton eines Intervalls setzen", "typ": "notieren", "symbol": "notieren",
  "anleitung": "Der untere Ton ist vorgegeben. Setze den oberen Ton. Wähle bei Bedarf vorher ♯ oder ♭.",
  "daten": {"vorzeichen": True, "aufgaben": [{"frage": f"{iv} über {T.name(a, True)}", "vorgabe": [a], "ziel": [T.ueber(a, iv)], "akkord": True}
                                             for a, iv in [("C4", "große Terz"), ("D4", "reine Quinte"), ("E4", "kleine Terz"), ("F4", "reine Quarte"), ("G4", "große Sexte"),
                                                           ("A4", "kleine Terz"), ("D4", "kleine Septime"), ("F4", "große Terz"), ("E4", "kleine Sexte"), ("G4", "reine Oktave")]]}},
 {"slug": "k9-halbtoene", "titel": "Zuordnen: Intervalle und Halbtöne", "kurz": "Wie viele Halbtöne hat welches Intervall?", "typ": "zuordnen", "symbol": "zuordnen",
  "anleitung": "Wähle zu jedem Intervall die Anzahl der Halbtöne.",
  "daten": {"paare": [{"links": n, "rechts": f"{h} Halbtöne" if h != 1 else "1 Halbton"} for n, h in [("kleine Sekunde", 1), ("große Sekunde", 2), ("kleine Terz", 3), ("große Terz", 4), ("reine Quarte", 5), ("Tritonus", 6), ("reine Quinte", 7), ("kleine Sexte", 8), ("große Sexte", 9), ("kleine Septime", 10), ("große Septime", 11), ("reine Oktave", 12)]]}},
],
}

# ======================================================================
DK_ARTEN = ["Dur", "Moll", "vermindert", "übermäßig"]


def dk(grund, art, dauer="1", label=""):
    t = T.dreiklang(grund, art)
    lab = ("@" + label.replace(" ", "_")) if label else ""
    return "[" + " ".join(t) + f"]/{dauer}{lab}"


def dk_name(grund, art):
    n = T.name(grund)
    if art == "Dur":
        return f"{n[0].upper() + n[1:]}-Dur-Dreiklang"
    if art == "Moll":
        return f"{n}-Moll-Dreiklang"
    return f"{art}er Dreiklang auf {n}"


def dk_frage(grund, art):
    opt = [art] + [a for a in DK_ARTEN if a != art]
    return {"frage": "Welcher Dreiklang ist das?", "noten": dk(grund, art), "optionen": [o + "-Dreiklang" if o in ("Dur", "Moll") else o + "er Dreiklang" for o in opt], "richtig": 0,
            "erklaerung": f"Grundton {T.name(grund)}: unten {T.intervall(*T.dreiklang(grund, art)[:2])}, oben {T.intervall(*T.dreiklang(grund, art)[1:])}."}


STUFEN_C = [("C4", "Dur", "I"), ("D4", "Moll", "II"), ("E4", "Moll", "III"), ("F4", "Dur", "IV"), ("G4", "Dur", "V"), ("A4", "Moll", "VI"), ("B4", "vermindert", "VII")]

KAPITEL[10] = {
"kurz": "Dreiklänge durch Terzschichtung: Dur, Moll, vermindert und übermäßig, Akkordsymbole und die Hauptdreiklänge einer Tonart.",
"inhalt": f"""
<p class="lead">Spielt man drei bestimmte Töne gleichzeitig, entsteht ein voller, runder Klang. Fast alle Lieder werden mit solchen <span class="fachwort">Dreiklängen</span> begleitet.</p>

<h2>Terzschichtung</h2>
<p>Ein Dreiklang entsteht, wenn man <strong>zwei Terzen übereinander</strong> schichtet. Die drei Töne heißen:</p>
<ul>
  <li><strong>Grundton</strong> (gibt dem Dreiklang den Namen),</li>
  <li><strong>Terz</strong> (eine Terz über dem Grundton),</li>
  <li><strong>Quinte</strong> (eine Quinte über dem Grundton).</li>
</ul>
<p>Im Notenbild sieht ein Dreiklang in Grundstellung aus wie ein Schneemann: Alle drei Noten liegen auf Linien oder alle in Zwischenräumen.</p>
{N(dk("C4", "Dur", label="c-e-g") + " " + dk("D4", "Moll", label="d-f-a") + " " + dk("E4", "Moll", label="e-g-h") + " " + dk("F4", "Dur", label="f-a-c"), "Terzschichtung: jeweils zwei Terzen übereinander", zoom=1.6)}

<h2>Vier Arten von Dreiklängen</h2>
<p>Je nachdem, ob die Terzen groß oder klein sind, klingt der Dreiklang anders:</p>
<div class="tabelle-scroll"><table>
  <thead><tr><th>Dreiklang</th><th>untere Terz</th><th>obere Terz</th><th>Rahmen</th><th>Beispiel</th></tr></thead>
  <tbody>
    <tr><td><strong>Dur</strong></td><td>groß (4)</td><td>klein (3)</td><td>reine Quinte</td><td>c – e – g</td></tr>
    <tr><td><strong>Moll</strong></td><td>klein (3)</td><td>groß (4)</td><td>reine Quinte</td><td>c – es – g</td></tr>
    <tr><td><strong>vermindert</strong></td><td>klein (3)</td><td>klein (3)</td><td>verminderte Quinte</td><td>c – es – ges</td></tr>
    <tr><td><strong>übermäßig</strong></td><td>groß (4)</td><td>groß (4)</td><td>übermäßige Quinte</td><td>c – e – gis</td></tr>
  </tbody>
</table></div>
{N(dk("C4", "Dur", label="Dur") + " " + dk("C4", "Moll", label="Moll") + " " + dk("C4", "vermindert", label="vermindert") + " " + dk("C4", "übermäßig", label="übermäßig"), "Die vier Dreiklangsarten auf c", zoom=1.6)}
<p>Dur- und Moll-Dreiklang unterscheiden sich nur in der <strong>Terz</strong>: Dur hat unten die große Terz, Moll die kleine. Dur klingt meist hell und fröhlich, Moll eher dunkel und ernst.</p>

<h2>Einen Dreiklang bilden</h2>
<p>Beispiel: Dur-Dreiklang auf d.</p>
<ol>
  <li>Grundton notieren: d′.</li>
  <li>Terzen schichten: d′ – f′ – a′.</li>
  <li>Halbtöne prüfen: d–f sind nur 3 Halbtöne (kleine Terz). Für Dur braucht man 4, also <strong>fis</strong>. fis–a sind 3 Halbtöne, passt.</li>
  <li>Ergebnis: D-Dur-Dreiklang = d – fis – a.</li>
</ol>

<h2>Akkordsymbole</h2>
<p>In Liederbüchern und Leadsheets stehen über den Noten <span class="fachwort">Akkordsymbole</span>:</p>
<ul>
  <li><strong>C</strong> = C-Dur-Dreiklang (großer Buchstabe allein)</li>
  <li><strong>Cm</strong> oder <strong>c</strong> = c-Moll-Dreiklang</li>
  <li><strong>C°</strong> oder <strong>Cdim</strong> = verminderter Dreiklang</li>
  <li><strong>C+</strong> oder <strong>Caug</strong> = übermäßiger Dreiklang</li>
</ul>
<p>Achtung: In englischen Akkordsymbolen steht B für den Ton h. Ein „B“ über den Noten meint also meist den H-Dur-Dreiklang, „Bb“ den B-Dur-Dreiklang.</p>

<h2>Die Dreiklänge einer Tonart</h2>
<p>Baut man auf jeder Stufe einer Dur-Tonleiter einen Dreiklang nur aus Tönen der Tonleiter, entstehen <strong>leitereigene Dreiklänge</strong>:</p>
{N(" ".join(dk(g_, a, label=f"{s}") for g_, a, s in STUFEN_C), "C-Dur: Dur-Dreiklänge auf I, IV und V, Moll-Dreiklänge auf II, III und VI, ein verminderter auf VII", zoom=1.6)}
<p>Die drei Dur-Dreiklänge auf der I., IV. und V. Stufe heißen <span class="fachwort">Hauptdreiklänge</span>:</p>
<ul>
  <li><strong>Tonika (T)</strong> auf der I. Stufe – Ruhe, „zu Hause“</li>
  <li><strong>Subdominante (S)</strong> auf der IV. Stufe</li>
  <li><strong>Dominante (D)</strong> auf der V. Stufe – Spannung, die zur Tonika zurückdrängt</li>
</ul>
<p>Mit diesen drei Akkorden lassen sich viele einfache Lieder begleiten. Im Quintenzirkel liegen Subdominante und Dominante direkt neben der Tonika.</p>
<p>Ein Dreiklang muss nicht immer mit dem Grundton unten stehen. Liegt die Terz unten, heißt das <strong>Sextakkord</strong>, liegt die Quinte unten, <strong>Quartsextakkord</strong>. Man spricht von <strong>Umkehrungen</strong>.</p>
{N(dk("C4", "Dur", label="Grundstellung") + " [E4 G4 C5]/1@Sextakkord [G4 C5 E5]/1@Quartsextakkord", "C-Dur-Dreiklang in Grundstellung und Umkehrungen", zoom=1.6)}

<div class="merke"><strong>Merke</strong>
<p>Dreiklänge entstehen durch Terzschichtung: Grundton, Terz, Quinte. Dur = große + kleine Terz, Moll = kleine + große Terz, vermindert = zwei kleine, übermäßig = zwei große Terzen. Die Hauptdreiklänge einer Dur-Tonart stehen auf der I. (Tonika), IV. (Subdominante) und V. Stufe (Dominante).</p></div>
""",
"aufgaben": [
 ("I", "Erkläre, was man unter Terzschichtung versteht, und benenne die drei Töne eines Dreiklangs.", 3, ""),
 ("I", "Bestimme die Art der Dreiklänge (Dur, Moll, vermindert, übermäßig).", 0, N(" ".join(dk(g_, a) for g_, a in [("F4", "Dur"), ("A4", "Moll"), ("D4", "Dur"), ("B4", "vermindert"), ("E4", "Moll"), ("C4", "übermäßig"), ("G4", "Dur"), ("D4", "Moll")]), zoom=1.5)),
 ("II", "Notiere die Dreiklänge: G-Dur, e-Moll, A-Dur, d-Moll, F-Dur, h-vermindert.", 0, N("", breite=520)),
 ("II", "Notiere die Hauptdreiklänge von G-Dur und F-Dur und beschrifte sie mit T, S und D.", 0, N("", tonart=1, breite=520) + N("", tonart=-1, breite=520)),
 ("II", "Begleite das Lied „Bruder Jakob“ (F-Dur) nur mit dem Akkord F. Probiert danach, mit welchen Akkorden sich „Alle meine Entchen“ in C-Dur begleiten lässt.", 0, ""),
 ("III", "Erkläre, warum der Dreiklang auf der VII. Stufe einer Dur-Tonleiter vermindert ist.", 4, ""),
],
"uebungen": [
 {"slug": "k10-bestimmen", "titel": "Dreiklänge bestimmen", "kurz": "Dur, Moll, vermindert oder übermäßig?", "typ": "notenquiz", "symbol": "dreiklaenge",
  "anleitung": "Bestimme die Art des Dreiklangs. Mit „Anhören“ kannst du ihn dir vorspielen lassen.",
  "daten": {"hoeren": True, "fragen": [dk_frage(g_, a) for g_, a in [("C4", "Dur"), ("A4", "Moll"), ("D4", "Moll"), ("G4", "Dur"), ("B4", "vermindert"), ("F4", "Dur"), ("E4", "Moll"), ("C4", "übermäßig"),
                                                                     ("D4", "Dur"), ("C4", "Moll"), ("E4", "Dur"), ("F#4", "vermindert")]]}},
 {"slug": "k10-notieren", "titel": "Dreiklänge notieren", "kurz": "Terz und Quinte über den Grundton setzen", "typ": "notieren", "symbol": "notieren",
  "anleitung": "Der Grundton ist vorgegeben. Setze Terz und Quinte darüber. Wähle bei Bedarf vorher ♯ oder ♭.",
  "daten": {"vorzeichen": True, "aufgaben": [{"frage": dk_name(g_, a), "vorgabe": [g_], "ziel": T.dreiklang(g_, a)[1:], "akkord": True}
                                             for g_, a in [("C4", "Dur"), ("F4", "Dur"), ("G4", "Dur"), ("A4", "Moll"), ("D4", "Moll"), ("E4", "Moll"), ("D4", "Dur"), ("A4", "Dur"), ("G4", "Moll"), ("B4", "vermindert")]]}},
 {"slug": "k10-symbole", "titel": "Zuordnen: Akkordsymbole", "kurz": "Akkordsymbole und Töne", "typ": "zuordnen", "symbol": "zuordnen",
  "anleitung": "Welche Töne gehören zu welchem Akkordsymbol?",
  "daten": {"paare": [{"links": s, "rechts": " – ".join(T.name(t) for t in T.dreiklang(g_, a))} for s, g_, a in [("C", "C4", "Dur"), ("G", "G4", "Dur"), ("F", "F4", "Dur"), ("Am", "A4", "Moll"), ("Dm", "D4", "Moll"), ("Em", "E4", "Moll"), ("D", "D4", "Dur"), ("Cm", "C4", "Moll"), ("H°", "B4", "vermindert")]]}},
 {"slug": "k10-hauptdreiklaenge", "titel": "Quiz: Hauptdreiklänge", "kurz": "Tonika, Subdominante und Dominante", "typ": "notenquiz", "symbol": "quiz",
  "anleitung": "Wähle die richtige Antwort.",
  "daten": {"fragen": [
   {"frage": "Auf welchen Stufen stehen die Hauptdreiklänge?", "optionen": ["I, IV und V", "I, II und III", "I, III und V", "II, V und VI"], "richtig": 0, "erklaerung": "Tonika, Subdominante, Dominante."},
   {"frage": "Wie heißt die Dominante in C-Dur?", "optionen": ["G-Dur", "F-Dur", "D-Dur", "a-Moll"], "richtig": 0, "erklaerung": "V. Stufe von C-Dur: g."},
   {"frage": "Wie heißt die Subdominante in G-Dur?", "optionen": ["C-Dur", "D-Dur", "F-Dur", "e-Moll"], "richtig": 0, "erklaerung": "IV. Stufe von G-Dur: c."},
   {"frage": "Welche Töne hat die Dominante von F-Dur?", "optionen": ["c – e – g", "b – d – f", "f – a – c", "g – h – d"], "richtig": 0, "erklaerung": "V. Stufe von F-Dur ist c, also C-Dur."},
   {"frage": "Welcher Dreiklang klingt am meisten nach „Schluss“?", "optionen": ["Tonika", "Dominante", "Subdominante", "verminderter Dreiklang"], "richtig": 0, "erklaerung": "Die Tonika ist das „Zuhause“ der Tonart."},
   {"frage": "Welche Art hat der Dreiklang auf der II. Stufe in Dur?", "optionen": ["Moll", "Dur", "vermindert", "übermäßig"], "richtig": 0, "erklaerung": "In C-Dur: d – f – a."},
   {"frage": "Welche Umkehrung ist das?", "noten": "[E4 G4 C5]/1", "optionen": ["Sextakkord", "Grundstellung", "Quartsextakkord"], "richtig": 0, "erklaerung": "Die Terz e liegt unten."}
  ]}},
],
}
