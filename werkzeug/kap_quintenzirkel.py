"""Kapitel 12: Der Quintenzirkel – und das Abschlusstraining."""
import math
from notensatz import N, svg as noten_svg
from zeichnungen import svg, text
import theorie as T

KREIS = [0, 1, 2, 3, 4, 5, 6, -5, -4, -3, -2, -1]   # im Uhrzeigersinn ab C


def zirkel_bild():
    cx, cy, r1, r2, r3 = 260, 260, 230, 165, 100
    i = f'<circle class="s f-weiss" cx="{cx}" cy="{cy}" r="{r1}"/><circle class="s2 f-gelb-weich" cx="{cx}" cy="{cy}" r="{r2}"/><circle class="s2 f-blau-weich" cx="{cx}" cy="{cy}" r="{r3}"/>'
    for k, vz in enumerate(KREIS):
        w = math.radians(-90 + k * 30)
        w2 = math.radians(-90 + k * 30 + 15)
        i += f'<line class="s2 nl-blass" x1="{cx + math.cos(w2) * r3:.1f}" y1="{cy + math.sin(w2) * r3:.1f}" x2="{cx + math.cos(w2) * r1:.1f}" y2="{cy + math.sin(w2) * r1:.1f}"/>'
        dur, moll = T.TONARTEN[vz]
        if vz == 6:
            dur, moll = "Fis/Ges", "dis/es"
        i += text(round(cx + math.cos(w) * (r1 + r2) / 2, 1), round(cy + math.sin(w) * (r1 + r2) / 2 + 2, 1), dur.replace("-Dur", ""), "h zk-dur")
        vzt = "" if vz == 0 else (f"{vz} ♯" if vz > 0 else f"{-vz} ♭")
        if vz == 6:
            vzt = "6 ♯ / 6 ♭"
        i += text(round(cx + math.cos(w) * (r1 + r2) / 2, 1), round(cy + math.sin(w) * (r1 + r2) / 2 + 24, 1), vzt, "hk zk-vz")
        i += text(round(cx + math.cos(w) * (r2 + r3) / 2, 1), round(cy + math.sin(w) * (r2 + r3) / 2 + 6, 1), moll.replace("-Moll", ""), "hk zk-moll")
    i += text(cx, cy - 10, "Dur außen", "hk") + text(cx, cy + 14, "Moll innen", "hk")
    i += f'<path class="s2 k-rosa" fill="none" stroke-width="3" d="M{cx + 70} {cy - r1 - 14} A {r1 + 14} {r1 + 14} 0 0 1 {cx + r1 + 4} {cy - 80}"/>' + text(cx + 210, cy - r1 + 4, "+1 ♯", "hk k-rosa-t")
    i += f'<path class="s2 k-blau" fill="none" stroke-width="3" d="M{cx - 70} {cy - r1 - 14} A {r1 + 14} {r1 + 14} 0 0 0 {cx - r1 - 4} {cy - 80}"/>' + text(cx - 210, cy - r1 + 4, "+1 ♭", "hk k-blau-t")
    return svg("-20 -10 560 540", i, "Der Quintenzirkel",
               "Ein Kreis mit zwölf Feldern. Oben C-Dur und a-Moll ohne Vorzeichen. Im Uhrzeigersinn kommt mit jeder Quinte ein Kreuz dazu: G, D, A, E, H, Fis. Gegen den Uhrzeigersinn kommt jeweils ein b dazu: F, B, Es, As, Des, Ges. Innen stehen die parallelen Moll-Tonarten.")


def vorzeichen_reihe(vorzeichen, beschriften=True):
    zellen = ""
    for vz in vorzeichen:
        dur, moll = T.TONARTEN[vz]
        zellen += f'<div class="vz-zelle">{noten_svg("", tonart=vz, breite=110 if abs(vz) > 3 else 90, zoom=1.3, oben=3, unten=2.5, titel=dur if beschriften else "Generalvorzeichen")}{f"<span>{dur}<br><small>{moll}</small></span>" if beschriften else "<span>______-Dur<br><small>______-Moll</small></span>"}</div>'
    return f'<div class="vz-reihe">{zellen}</div>'


def tonart_frage(vz):
    dur = T.TONARTEN[vz][0]
    andere = [T.TONARTEN[k][0] for k in (vz + 1, vz - 1, -vz if vz else 2) if k in T.TONARTEN and T.TONARTEN[k][0] != dur]
    andere = list(dict.fromkeys(andere))
    while len(andere) < 3:
        for k in T.TONARTEN:
            if T.TONARTEN[k][0] not in andere and T.TONARTEN[k][0] != dur:
                andere.append(T.TONARTEN[k][0])
                break
    vzt = "keine Vorzeichen" if vz == 0 else (f"{vz} Kreuz" + ("e" if vz > 1 else "") if vz > 0 else f"{-vz} b")
    return {"frage": "Welche Dur-Tonart hat diese Vorzeichen?", "noten": "", "spec": {"tonart": vz, "breite": 120 if abs(vz) > 3 else 100},
            "optionen": [dur] + andere[:3], "richtig": 0, "erklaerung": f"{vzt}: {dur} (parallel: {T.TONARTEN[vz][1]})."}


KAPITEL = {}

KAPITEL[12] = {
"kurz": "Wie die Tonarten zusammenhängen: Kreuz- und b-Tonarten, Reihenfolge der Vorzeichen, Paralleltonarten und Tonarten bestimmen.",
"inhalt": f"""
<p class="lead">Es gibt viele Dur- und Moll-Tonarten. Der <span class="fachwort">Quintenzirkel</span> ordnet sie alle in einem Kreis an. Damit erkennt man auf einen Blick, wie viele Vorzeichen eine Tonart hat und welche Tonarten miteinander verwandt sind.</p>

<h2>Warum Quinten?</h2>
<p>Erinnere dich an den Bauplan der Dur-Tonleiter (Kapitel 8): Sie besteht aus zwei gleich gebauten Hälften mit dem Muster 1 – 1 – ½. Die <strong>obere Hälfte von C-Dur</strong> (g – a – h – c) ist gleichzeitig die <strong>untere Hälfte von G-Dur</strong>. G liegt eine <strong>Quinte</strong> über C.</p>
{N("C4/1 {GT} D4/1 {GT} E4/1 {HT} F4/1 || *G4/1 {GT} *A4/1 {GT} *B4/1 {HT} *C5/1 {GT} D5/1 {GT} E5/1 {HT} F#5/1 {HT} G5/1", "Die obere Hälfte von C-Dur ist die untere Hälfte von G-Dur. In der neuen oberen Hälfte muss f zu fis erhöht werden.", zoom=1.4)}
<p>Für die neue obere Hälfte muss man genau <strong>einen Ton erhöhen</strong>: die 7. Stufe. So kommt mit jedem Schritt eine Quinte nach oben ein Kreuz dazu: C (0) → G (1 ♯) → D (2 ♯) → A (3 ♯) → E (4 ♯) → H (5 ♯) → Fis (6 ♯).</p>
<p>Geht man von C aus eine Quinte <strong>abwärts</strong>, kommt jedes Mal ein <strong>b</strong> dazu: C (0) → F (1 ♭) → B (2 ♭) → Es (3 ♭) → As (4 ♭) → Des (5 ♭) → Ges (6 ♭).</p>

<h2>Der Kreis</h2>
<figure class="breit zirkel"><div class="bild">{zirkel_bild()}</div><figcaption>Der Quintenzirkel: im Uhrzeigersinn je eine Quinte höher und ein Kreuz mehr, gegen den Uhrzeigersinn je ein b mehr</figcaption></figure>
<ul>
  <li><strong>Außen</strong> stehen die Dur-Tonarten, <strong>innen</strong> ihre parallelen Moll-Tonarten mit denselben Vorzeichen.</li>
  <li>Unten treffen sich Fis-Dur (6 ♯) und Ges-Dur (6 ♭). Sie klingen gleich, nur die Schreibweise unterscheidet sich (enharmonische Verwechslung). Dadurch schließt sich der Kreis.</li>
  <li>Ein möglicher Merksatz für die Kreuz-Tonarten: „<strong>G</strong>eh <strong>D</strong>u <strong>A</strong>lter <strong>E</strong>sel, <strong>H</strong>ol <strong>Fis</strong>che.“ Für die b-Tonarten: „<strong>F</strong>rische <strong>B</strong>rötchen <strong>Es</strong>sen <strong>As</strong>tronauten <strong>Des</strong> <strong>Ges</strong>chmacks wegen.“ Am besten erfindet ihr eigene Merksätze.</li>
</ul>
<p><a class="knopf leise" href="../werkzeuge/quintenzirkel.html">Interaktiven Quintenzirkel öffnen</a></p>

<h2>Die Reihenfolge der Vorzeichen</h2>
<p>Die Vorzeichen kommen immer in derselben Reihenfolge dazu und stehen auch so hinter dem Schlüssel:</p>
<ul>
  <li><strong>Kreuze:</strong> fis – cis – gis – dis – ais – eis (jeweils eine Quinte höher)</li>
  <li><strong>B’s:</strong> b – es – as – des – ges – ces (jeweils eine Quinte tiefer, also genau umgekehrt)</li>
</ul>
{vorzeichen_reihe([0, 1, 2, 3, 4, 5, 6])}
{vorzeichen_reihe([-1, -2, -3, -4, -5, -6])}

<h2>Tonart aus den Vorzeichen bestimmen</h2>
<p>Zwei Tricks helfen, ohne den ganzen Kreis aufzumalen:</p>
<ul>
  <li><strong>Kreuz-Tonarten:</strong> Das <strong>letzte Kreuz</strong> ist die 7. Stufe. Einen Halbton darüber liegt der Grundton. Beispiel: letztes Kreuz gis → A-Dur.</li>
  <li><strong>b-Tonarten:</strong> Das <strong>vorletzte b</strong> ist der Grundton. Beispiel: b, es, as → vorletztes ist es → Es-Dur. Nur F-Dur (ein b) muss man sich merken.</li>
</ul>
<p>Dieselben Vorzeichen gehören immer zu einer Dur-Tonart <strong>und</strong> ihrer parallelen Moll-Tonart. Ob ein Stück in Dur oder Moll steht, verrät meist der <strong>Schlusston</strong> und der Klang:</p>
{N("E4/4 G4/4 B4/4 G4/4 | F4/4 D4/4 B3/2 | E4/4 F4/4 G4/4 F4/4 | E4/1 |.", "Ein Kreuz: G-Dur oder e-Moll? Die Melodie endet auf e und klingt nach Moll: e-Moll.", tonart=1, takt="4/4", zoom=1.4)}

<h2>Was der Quintenzirkel noch zeigt</h2>
<ul>
  <li><strong>Verwandte Tonarten:</strong> Benachbarte Tonarten unterscheiden sich nur in einem Vorzeichen. Ein Stück kann deshalb leicht in eine Nachbartonart wechseln (Modulation).</li>
  <li><strong>Hauptdreiklänge:</strong> Links neben der Tonika steht die <strong>Subdominante</strong>, rechts die <strong>Dominante</strong>. In C-Dur: F – C – G. Zusammen mit den Moll-Tonarten darunter (d, a, e) hat man alle sechs Dur- und Moll-Dreiklänge der Tonart beisammen.</li>
</ul>

<div class="merke"><strong>Merke</strong>
<p>Im Quintenzirkel sind die Tonarten im Quintabstand angeordnet. Im Uhrzeigersinn (Quinte aufwärts) kommt je ein Kreuz dazu, gegen den Uhrzeigersinn (Quinte abwärts) je ein b. Reihenfolge der Kreuze: fis cis gis dis ais eis; der b’s: b es as des ges ces. Letztes Kreuz + Halbton = Dur-Grundton; vorletztes b = Dur-Grundton. Innen stehen die parallelen Moll-Tonarten.</p></div>
""",
"aufgaben": [
 ("I", "Zeichne den Quintenzirkel mit allen Dur- und Moll-Tonarten und der Anzahl der Vorzeichen.", 0, ""),
 ("I", "Nenne die Reihenfolge der Kreuze und der b’s.", 2, ""),
 ("II", "Bestimme die Dur-Tonart und ihre parallele Moll-Tonart.", 0, vorzeichen_reihe([2, -3, 4, -1, 3, -4], beschriften=False)),
 ("II", "Notiere die Generalvorzeichen für A-Dur, B-Dur, h-Moll und c-Moll.", 0, N("", breite=520)),
 ("II", "Erkläre mit dem Aufbau der Dur-Tonleiter aus zwei Hälften, warum im Uhrzeigersinn jeweils ein Kreuz dazukommt.", 6, ""),
 ("II", "Nenne zu D-Dur und Es-Dur jeweils Tonika, Subdominante und Dominante. Nutze den Quintenzirkel.", 3, ""),
 ("III", "Ein Lied hat zwei b als Generalvorzeichen und endet auf g. Bestimme die Tonart und begründe.", 4, ""),
 ("III", "Erfindet eigene Merksätze für die Reihenfolge der Kreuz- und b-Tonarten und stellt sie der Klasse vor.", 0, ""),
],
"uebungen": [
 {"slug": "k11-tonart-bestimmen", "titel": "Tonarten an den Vorzeichen erkennen", "kurz": "Generalvorzeichen lesen und die Dur-Tonart nennen", "typ": "notenquiz", "symbol": "quintenzirkel",
  "anleitung": "Welche Dur-Tonart hat diese Vorzeichen? Denk an die Tricks: letztes Kreuz + Halbton, vorletztes b.",
  "daten": {"fragen": [tonart_frage(v) for v in [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0, 6]]}},
 {"slug": "k11-vorzeichen", "titel": "Zuordnen: Tonarten und Vorzeichen", "kurz": "Wie viele Vorzeichen hat welche Tonart?", "typ": "zuordnen", "symbol": "zuordnen",
  "anleitung": "Wähle zu jeder Tonart die richtigen Vorzeichen.",
  "daten": {"paare": [
   {"links": "G-Dur", "rechts": "fis"}, {"links": "D-Dur", "rechts": "fis, cis"}, {"links": "A-Dur", "rechts": "fis, cis, gis"}, {"links": "E-Dur", "rechts": "fis, cis, gis, dis"},
   {"links": "F-Dur", "rechts": "b"}, {"links": "B-Dur", "rechts": "b, es"}, {"links": "Es-Dur", "rechts": "b, es, as"}, {"links": "As-Dur", "rechts": "b, es, as, des"}, {"links": "C-Dur", "rechts": "keine"}
  ]}},
 {"slug": "k11-reihenfolge", "titel": "Reihenfolge: Rund um den Quintenzirkel", "kurz": "Kreuz-Tonarten im Uhrzeigersinn ordnen", "typ": "reihenfolge", "symbol": "sortieren",
  "anleitung": "Bringe die Dur-Tonarten in die Reihenfolge des Quintenzirkels, beginnend bei C im Uhrzeigersinn.",
  "daten": {"schritte": ["C-Dur (keine Vorzeichen)", "G-Dur", "D-Dur", "A-Dur", "E-Dur", "H-Dur", "Fis-Dur"]}},
 {"slug": "k11-reihenfolge-b", "titel": "Reihenfolge: Die b-Tonarten", "kurz": "b-Tonarten gegen den Uhrzeigersinn ordnen", "typ": "reihenfolge", "symbol": "sortieren",
  "anleitung": "Bringe die Dur-Tonarten in die Reihenfolge des Quintenzirkels, beginnend bei C gegen den Uhrzeigersinn.",
  "daten": {"schritte": ["C-Dur (keine Vorzeichen)", "F-Dur", "B-Dur", "Es-Dur", "As-Dur", "Des-Dur", "Ges-Dur"]}},
 {"slug": "k11-quiz", "titel": "Quiz: Quintenzirkel", "kurz": "Parallele Tonarten, Hauptdreiklänge und Tonart eines Liedes", "typ": "notenquiz", "symbol": "quiz",
  "anleitung": "Wähle die richtige Antwort.",
  "daten": {"fragen": [
   {"frage": "Welche Tonart liegt im Quintenzirkel rechts neben D-Dur?", "optionen": ["A-Dur", "G-Dur", "E-Dur", "h-Moll"], "richtig": 0, "erklaerung": "Eine Quinte über d liegt a."},
   {"frage": "Welche Moll-Tonart hat drei b?", "optionen": ["c-Moll", "g-Moll", "f-Moll", "es-Moll"], "richtig": 0, "erklaerung": "Parallel zu Es-Dur."},
   {"frage": "Welche Moll-Tonart hat zwei Kreuze?", "optionen": ["h-Moll", "e-Moll", "fis-Moll", "d-Moll"], "richtig": 0, "erklaerung": "Parallel zu D-Dur."},
   {"frage": "Welches Kreuz kommt als drittes dazu?", "optionen": ["gis", "dis", "cis", "fis"], "richtig": 0, "erklaerung": "fis – cis – gis – dis …"},
   {"frage": "Welches b kommt als viertes dazu?", "optionen": ["des", "as", "ges", "es"], "richtig": 0, "erklaerung": "b – es – as – des …"},
   {"frage": "Was sind Tonika, Subdominante und Dominante in G-Dur?", "optionen": ["G, C, D", "G, D, A", "G, F, C", "G, e, h"], "richtig": 0, "erklaerung": "Links von G steht C, rechts D."},
   {"frage": "Welche Tonarten klingen gleich, werden aber anders geschrieben?", "optionen": ["Fis-Dur und Ges-Dur", "G-Dur und e-Moll", "C-Dur und a-Moll", "F-Dur und B-Dur"], "richtig": 0, "erklaerung": "Enharmonische Verwechslung. G-Dur/e-Moll sind parallel, das ist etwas anderes."},
   {"frage": "In welcher Tonart steht das Lied wahrscheinlich?", "noten": "D4/4 F4/4 A4/4 F4/4 | G4/4 E4/4 C#4/2 | D4/1 |.", "spec": {"tonart": -1, "takt": "4/4"}, "optionen": ["d-Moll", "F-Dur", "D-Dur", "B-Dur"], "richtig": 0, "erklaerung": "Ein b (F-Dur oder d-Moll), Schlusston d, cis als Leitton: d-Moll."},
   {"frage": "In welcher Tonart steht das Lied wahrscheinlich?", "noten": "D4/4 F#4/4 A4/4 D5/4 | C#5/4 A4/4 E4/2 | D4/1 |.", "spec": {"tonart": 2, "takt": "4/4"}, "optionen": ["D-Dur", "h-Moll", "A-Dur", "G-Dur"], "richtig": 0, "erklaerung": "Zwei Kreuze (D-Dur oder h-Moll), Schlusston d: D-Dur."},
   {"frage": "Warum kommt im Uhrzeigersinn jeweils ein Kreuz dazu?", "optionen": ["Die 7. Stufe der neuen Tonart muss erhöht werden.", "Weil Quinten immer Kreuze haben.", "Weil die Töne höher werden.", "Weil der Grundton erhöht wird."], "richtig": 0, "erklaerung": "Nur so liegt der Halbton zwischen 7. und 8. Stufe."}
  ]}},
 {"slug": "abschlusstest", "titel": "Abschlusstest Notenlehre", "kurz": "20 Fragen quer durch alle Kapitel", "typ": "notenquiz", "symbol": "quiz", "training": True,
  "anleitung": "Der große Test von den Notenwerten bis zum Quintenzirkel. Am Ende siehst du, wie viele du richtig hattest.",
  "daten": {"hoeren": True, "fragen": [
   {"frage": "Wie viele Achtel passen in einen 3/4-Takt?", "optionen": ["6", "3", "8", "4"], "richtig": 0, "erklaerung": "3 Viertel = 6 Achtel."},
   {"frage": "Was fehlt im 4/4-Takt?", "noten": "C4/4. C4/8 ?/2 |", "spec": {"rhythmus": True, "takt": "4/4"}, "optionen": [{"noten": "C4/2", "spec": {"rhythmus": True}}, {"noten": "C4/4", "spec": {"rhythmus": True}}, {"noten": "C4/2.", "spec": {"rhythmus": True}}, {"noten": "C4/8", "spec": {"rhythmus": True}}], "richtig": 0, "erklaerung": "1½ + ½ = 2, es fehlt eine Halbe."},
   {"frage": "Welche Pause liegt auf der Mittellinie?", "optionen": ["halbe Pause", "ganze Pause", "Viertelpause", "Achtelpause"], "richtig": 0, "erklaerung": "Die ganze hängt, die halbe liegt."},
   {"frage": "Eine Achteltriole dauert so lang wie …", "optionen": ["zwei Achtel", "drei Achtel", "eine halbe Note", "eine Sechzehntel"], "richtig": 0, "erklaerung": "Drei in der Zeit von zwei."},
   {"frage": "Wie heißt der Ton?", "noten": "A5/1", "optionen": ["a″", "a′", "f″", "c‴"], "richtig": 0, "erklaerung": "Auf der ersten Hilfslinie über dem System."},
   {"frage": "Wie heißt der Ton?", "noten": "E4/1", "optionen": ["e′", "g′", "c′", "f′"], "richtig": 0, "erklaerung": "Unterste Linie."},
   {"frage": "Wie heißt der Ton?", "noten": "Eb5/1", "optionen": ["es″", "ees″", "dis″", "e″"], "richtig": 0, "erklaerung": "e mit b heißt es."},
   {"frage": "Welcher Ton klingt gleich wie gis?", "optionen": ["as", "ges", "a", "g"], "richtig": 0, "erklaerung": "Enharmonische Verwechslung."},
   {"frage": "Was bedeutet mp?", "optionen": ["mittelleise", "sehr leise", "mittellaut", "laut"], "richtig": 0, "erklaerung": "mezzopiano."},
   {"frage": "Wo liegen in Dur die Halbtöne?", "optionen": ["3–4 und 7–8", "2–3 und 5–6", "1–2 und 4–5", "3–4 und 6–7"], "richtig": 0, "erklaerung": "1 – 1 – ½ – 1 – 1 – 1 – ½."},
   {"frage": "Welche Tonleiter ist das?", "noten": " ".join(f"{t}/1" for t in T.tonleiter("D4", T.MOLL)), "optionen": ["d-Moll (natürlich)", "D-Dur", "F-Dur", "d-Moll (harmonisch)"], "richtig": 0, "erklaerung": "Ein b, Grundton d, Halbtöne 2–3 und 5–6."},
   {"frage": "Welches Intervall ist das?", "noten": "[G4 E5]/1", "optionen": ["große Sexte", "kleine Sexte", "reine Quinte", "kleine Septime"], "richtig": 0, "erklaerung": "6 Stufen, 9 Halbtöne."},
   {"frage": "Welches Intervall ist das?", "noten": "[D4 F4]/1", "optionen": ["kleine Terz", "große Terz", "große Sekunde", "reine Quarte"], "richtig": 0, "erklaerung": "3 Stufen, 3 Halbtöne."},
   {"frage": "Wie viele Halbtöne hat eine reine Quinte?", "optionen": ["7", "5", "6", "8"], "richtig": 0, "erklaerung": "c–g: 7 Halbtöne."},
   {"frage": "Welcher Dreiklang ist das?", "noten": "[E4 G4 B4]/1", "optionen": ["Moll-Dreiklang", "Dur-Dreiklang", "verminderter Dreiklang", "übermäßiger Dreiklang"], "richtig": 0, "erklaerung": "e–g kleine Terz, g–h große Terz."},
   {"frage": "Welche Töne hat der D-Dur-Dreiklang?", "optionen": ["d – fis – a", "d – f – a", "d – f – as", "d – fis – ais"], "richtig": 0, "erklaerung": "Große Terz unten, kleine oben."},
   {"frage": "Welche Dur-Tonart hat drei Kreuze?", "optionen": ["A-Dur", "D-Dur", "E-Dur", "Es-Dur"], "richtig": 0, "erklaerung": "Letztes Kreuz gis + Halbton = a."},
   {"frage": "Welche Dur-Tonart hat diese Vorzeichen?", "noten": "", "spec": {"tonart": -4, "breite": 110}, "optionen": ["As-Dur", "Des-Dur", "Es-Dur", "f-Moll"], "richtig": 0, "erklaerung": "Vorletztes b: as. (f-Moll hat dieselben Vorzeichen, ist aber keine Dur-Tonart.)"},
   {"frage": "Was ist die parallele Moll-Tonart von A-Dur?", "optionen": ["fis-Moll", "a-Moll", "cis-Moll", "e-Moll"], "richtig": 0, "erklaerung": "Drei Halbtöne unter a liegt fis."},
   {"frage": "Was steht im Quintenzirkel links neben C-Dur?", "optionen": ["F-Dur, die Subdominante", "G-Dur, die Dominante", "a-Moll", "B-Dur"], "richtig": 0, "erklaerung": "Gegen den Uhrzeigersinn: F."}
  ]}},
],
}
