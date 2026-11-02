"""Erzeugt alle Seiten der Website. Aufruf: python3 bauen.py (im Ordner werkzeug)."""
import html, json, os, shutil
from basis import seite, uebung, REPO, KAPITEL, STUFEN
import zeichnungen as Z
import notensatz
from kap_rhythmus import KAPITEL as K1
from kap_tonhoehe import KAPITEL as K2
from kap_tonleitern import KAPITEL as K3
from kap_klang import KAPITEL as K4
from kap_quintenzirkel import KAPITEL as K5
from kap_bass import KAPITEL as K6

INHALT = {}
for k in (K1, K2, K3, K4, K5, K6):
    INHALT.update(k)

AFB_TEXT = {"I": "AFB I", "II": "AFB II", "III": "AFB III"}
SYMBOL = {1: "notenwerte", 2: "pausen", 3: "punktierung", 4: "violinschluessel", 5: "bassschluessel", 6: "vorzeichen", 7: "dynamik", 8: "tonleiter", 9: "moll", 10: "intervalle", 11: "dreiklaenge", 12: "quintenzirkel"}
KOPF = {1: 1, 2: 2, 3: 3, 4: 4, 5: "bass", 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11}
JS_NOTEN = ["assets/glyphen.js", "assets/noten.js", "assets/musik.js"]

# Freischaltung durch die Lehrkraft
with open(os.path.join(REPO, "freigabe.json"), encoding="utf-8") as f:
    _frei = json.load(f)
FREI = {int(k.split()[-1]) for k, v in _frei.items() if k.startswith("Kapitel") and v is True}

STUFENWEISE = _frei.get("Stufen nacheinander freischalten", True) is True
notensatz.glyphen_js(os.path.join(REPO, "assets", "glyphen.js"))

# Lernpfad für die Freischaltung der Stufen (wird im Browser ausgewertet)
_pfad = {"stufenweise": STUFENWEISE, "namen": {str(k): v[0] for k, v in STUFEN.items()}, "stufen": {}}
for _nr, _slug, _t, _st in KAPITEL:
    if _nr in FREI:
        _pfad["stufen"].setdefault(str(_st), []).extend(u["slug"] for u in INHALT[_nr]["uebungen"] if u["slug"] != "abschlusstest")
with open(os.path.join(REPO, "assets", "lernpfad.js"), "w", encoding="utf-8") as f:
    f.write("/* automatisch erzeugt aus freigabe.json und den Kapiteln */\nwindow.LERNPFAD = " + json.dumps(_pfad, ensure_ascii=False) + ";\n")

WERKZEUGE = [
    {"slug": "klaviatur", "titel": "Klaviatur", "kurz": "Töne, Intervalle, Tonleitern und Dreiklänge sehen und hören",
     "text": "Tippe auf die Tasten. Im Modus „Intervalle“ wählst du zwei Tasten und siehst, wie viele Halbtöne dazwischen liegen. Unter „Tonleitern und Dreiklänge“ kannst du dir jede Dur- und Moll-Tonleiter anzeigen und vorspielen lassen."},
    {"slug": "quintenzirkel", "titel": "Quintenzirkel", "kurz": "Tonarten, Vorzeichen und Hauptdreiklänge erkunden",
     "text": "Tippe auf eine Tonart. Du siehst ihre Vorzeichen, die Tonleiter und die Hauptdreiklänge, und kannst alles anhören. Mit den Pfeiltasten wanderst du durch den Kreis."},
    {"slug": "taktbaukasten", "titel": "Taktbaukasten", "kurz": "Rhythmen aus Notenwerten und Pausen bauen und anhören",
     "text": "Wähle eine Taktart und baue bis zu vier Takte aus Notenwerten und Pausen. Der Baukasten achtet darauf, dass jeder Takt genau voll wird. Mit „Abspielen“ hörst du deinen Rhythmus."},
    {"slug": "notentrainer", "titel": "Notentrainer", "kurz": "Noten, Intervalle, Tonarten und Dreiklänge im Schnelltraining",
     "text": "Zehn zufällige Aufgaben pro Runde. Wähle oben, was du üben möchtest. Jede Runde ist anders."},
]


def kurztitel(t):
    return t.split(": ", 1)[1] if ": " in t else t


def kachel_liste(eintraege, ordner, mit_nr=False, symbol_key="symbol"):
    zeilen = []
    for i, e in enumerate(eintraege):
        nr = f'<span class="nr">{i + 1}</span>' if mit_nr else ""
        zeilen.append(f'<li><a href="{ordner}/{e["slug"]}.html" data-uebung="{e["slug"]}"><span class="kachel">{Z.symbol(e.get(symbol_key, "quiz"))}{nr}</span>'
                      f'<span class="titel">{html.escape(kurztitel(e["titel"]))}</span><span class="info">{html.escape(e["kurz"])}</span></a></li>')
    return '<ul class="liste zweispaltig">' + "".join(zeilen) + "</ul>"


def kap_titel(nr):
    return KAPITEL[nr - 1][2]


# ======================================================================
# alte Seiten entfernen (gesperrte Kapitel dürfen nicht stehen bleiben)
for ordner in ("kapitel", "aufgaben", "uebungen", "werkzeuge"):
    shutil.rmtree(os.path.join(REPO, ordner), ignore_errors=True)

freie = [k for k in KAPITEL if k[0] in FREI]

# ======================================================================
# Kapitel, Aufgaben, Übungen
for nr, slug, titel, stufe in KAPITEL:
    if nr not in FREI:
        continue
    d = INHALT[nr]
    idx = [k[0] for k in freie].index(nr)
    vor = freie[idx - 1] if idx > 0 else None
    nach = freie[idx + 1] if idx < len(freie) - 1 else None
    stufe_name = STUFEN[stufe][0]
    ueb = d["uebungen"]
    ueb_liste = kachel_liste(ueb, "../uebungen")
    links = [f'<a href="{vor[1]}.html">Zurück: {html.escape(vor[2])}</a>' if vor else '<span></span>',
             f'<a href="{nach[1]}.html">Weiter: {html.escape(nach[2])}</a>' if nach else '<a href="../index.html">Zur Übersicht</a>']
    inhalt = f"""
<article class="spalte lerntext">
  <div class="lt-bild">{Z.kopf(KOPF[nr])}</div>
  <p class="kapitel-nr">Kapitel {nr} · {html.escape(stufe_name)}</p>
  <h1>{html.escape(titel)}</h1>
{d["inhalt"]}
  <section class="ueben" aria-labelledby="ueben-{nr}">
    <h2 id="ueben-{nr}">Jetzt üben</h2>
    {ueb_liste}
    <p class="knopfreihe"><a class="knopf" href="../aufgaben/{slug}.html">Aufgaben zum Kapitel (Arbeitsblatt)</a></p>
  </section>
  <nav class="weiter" aria-label="Weitere Kapitel">{links[0]}{links[1]}</nav>
</article>"""
    seite(f"kapitel/{slug}.html", f"Kapitel {nr}: {titel}", inhalt, stufe=stufe,
          krumen=[("Notenlehre", "../index.html"), (f"Kapitel {nr}", None)], beschreibung=d["kurz"], skripte=JS_NOTEN, sperre=True)

    items = []
    for afb, text, zeilen, figur in d["aufgaben"]:
        z = f'<div class="schreibzeilen" style="--zeilen:{zeilen}"></div>' if zeilen else ""
        fig = f'<div class="aufgabe-noten">{figur}</div>' if figur else ""
        items.append(f'<li><p>{html.escape(text)} <span class="afb" title="Anforderungsbereich {afb}">{AFB_TEXT[afb]}</span></p>{fig}{z}</li>')
    inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(SYMBOL[nr])}<h1>Aufgaben: {html.escape(titel)}</h1></div>
  <p class="legende">Grundlage ist <a href="../kapitel/{slug}.html">Kapitel {nr}: {html.escape(titel)}</a>.
  AFB I = wiedergeben, AFB II = anwenden und erklären, AFB III = beurteilen und gestalten.</p>
  <div class="knopfreihe nicht-drucken">
    <button class="knopf leise" type="button" onclick="window.print()">Als Arbeitsblatt drucken</button>
  </div>
  <p class="nur-druck">Name: ______________________________ &nbsp; Datum: ______________</p>
  <ol class="aufgaben">
    {''.join(items)}
  </ol>
  <nav class="weiter" aria-label="Navigation">
    <a href="../kapitel/{slug}.html">Zurück zum Kapitel</a>
    <a href="../index.html">Zur Übersicht</a>
  </nav>
</article>"""
    seite(f"aufgaben/{slug}.html", f"Aufgaben: {titel}", inhalt, stufe=stufe,
          krumen=[("Notenlehre", "../index.html"), (f"Kapitel {nr}", f"../kapitel/{slug}.html"), ("Aufgaben", None)], beschreibung=f"Aufgaben zu {titel}", sperre=True)

    for u in ueb:
        inhalt = f"""
<article class="spalte lerntext uebung-seite">
  <div class="uebung-kopf">{Z.symbol(u.get("symbol", "quiz"))}<h1>{html.escape(u["titel"])}</h1></div>
  <p class="lead">{html.escape(u["anleitung"])}</p>
  {uebung(u["typ"], u["daten"], u["slug"])}
  <noscript><p>Für diese Übung muss JavaScript im Browser aktiviert sein.</p></noscript>
  <nav class="weiter" aria-label="Navigation"><a href="../kapitel/{slug}.html">Zurück zu Kapitel {nr}</a><a href="../index.html">Zur Übersicht</a></nav>
</article>"""
        seite(f"uebungen/{u['slug']}.html", u["titel"], inhalt, stufe=stufe,
              krumen=[("Notenlehre", "../index.html"), (f"Kapitel {nr}", f"../kapitel/{slug}.html"), ("Übung", None)],
              beschreibung=u["kurz"], skripte=["assets/uebungen.js"] + JS_NOTEN, sperre=True)

# ======================================================================
# Werkzeuge
for w in WERKZEUGE:
    inhalt = f"""
<article class="spalte breit-spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(w["slug"])}<h1>{html.escape(w["titel"])}</h1></div>
  <p class="lead">{html.escape(w["text"])}</p>
  <div class="modell werkzeug" data-werkzeug="{w["slug"]}"></div>
  <noscript><p>Für dieses Werkzeug muss JavaScript im Browser aktiviert sein.</p></noscript>
  <p class="legende">Den Klang erzeugt dein Browser selbst. Schalte den Ton ein, falls du nichts hörst.</p>
  <nav class="weiter" aria-label="Navigation"><a href="../index.html">Zur Übersicht</a></nav>
</article>"""
    seite(f"werkzeuge/{w['slug']}.html", w["titel"], inhalt, stufe=5 if w["slug"] == "quintenzirkel" else 1 if w["slug"] == "taktbaukasten" else 3,
          krumen=[("Notenlehre", "../index.html"), (w["titel"], None)], beschreibung=w["kurz"], skripte=JS_NOTEN)

# ======================================================================
# Startseite: Lernpfad
pfad = []
for stufe, (sname, klasse) in STUFEN.items():
    karten = []
    for nr, slug, titel, st in KAPITEL:
        if st != stufe:
            continue
        frei = nr in FREI
        d = INHALT[nr]
        anzahl = len(d["uebungen"])
        if frei:
            karten.append(f'<li><a class="kap-karte" href="kapitel/{slug}.html"><span class="kachel">{Z.symbol(SYMBOL[nr])}<span class="nr">{nr}</span></span>'
                          f'<span class="titel">{html.escape(titel)}</span><span class="info">{html.escape(d["kurz"])}</span>'
                          f'<span class="kap-meta">Lerntext · {anzahl} Übungen · Arbeitsblatt</span></a></li>')
        else:
            karten.append(f'<li><div class="kap-karte gesperrt"><span class="kachel">{Z.symbol(SYMBOL[nr])}<span class="nr">{nr}</span></span>'
                          f'<span class="titel">{html.escape(titel)}</span><span class="info">Noch nicht freigeschaltet.</span></div></li>')
    pfad.append(f"""
  <section class="stufe reihe-{stufe}" data-stufe="{stufe}" aria-labelledby="stufe-{stufe}">
    <div class="stufe-kopf"><span class="stufe-nr">Stufe {stufe}</span><h2 id="stufe-{stufe}">{html.escape(sname)}</h2><span class="stufe-klasse">{html.escape(klasse)}</span></div>
    <p class="stufe-stand" aria-live="polite"></p><p class="stufe-sperre" hidden></p>
    <ul class="kap-liste">{''.join(karten)}</ul>
  </section>""")

abschluss = ""
if 12 in FREI:
    abschluss = '<p class="knopfreihe"><a class="knopf" href="uebungen/abschlusstest.html">Abschlusstest: 20 Fragen quer durch alle Kapitel</a></p>'

seite("index.html", "Notenlehre", f"""
<section class="buehne">
  <div class="huelle">
    <div>
      <p class="unterzeile">Musik · Klasse 10</p>
      <h1>Noten&shy;lehre</h1>
      <p class="einleitung">Von den Notenwerten bis zum Quintenzirkel: alles, was ihr seit Klasse 7 gelernt habt, Schritt für Schritt wiederholt. Mit Lerntexten, Übungen zum Anklicken und Anhören, Arbeitsblättern und Werkzeugen zum Ausprobieren.</p>
    </div>
    {Z.hero_bild()}
  </div>
</section>
<div class="huelle">
  <section class="bereich" aria-labelledby="pfad">
    <h2 id="pfad">Der Lernpfad</h2>
    <p class="hinweis">Die Kapitel bauen aufeinander auf.{" Jede Stufe wird freigeschaltet, sobald du alle Übungen der vorherigen Stufe gelöst hast (mindestens 80 Prozent richtig)." if STUFENWEISE else " Wer unsicher ist, fängt vorne an; wer schon sicher ist, springt direkt zu seinem Thema."}</p>
    <p class="legende" id="fortschritt-info">Dein Fortschritt wird nur in diesem Browser auf diesem Gerät gespeichert. Auf einem anderen Gerät beginnst du wieder bei Stufe 1. <button class="knopf leise klein" type="button" id="fortschritt-reset">Fortschritt zurücksetzen</button></p>
    <div class="lernpfad">{''.join(pfad)}</div>
    {abschluss}
  </section>
  <section class="bereich reihe-3" aria-labelledby="werkzeuge">
    <h2 id="werkzeuge">Werkzeuge zum Ausprobieren</h2>
    <p class="hinweis">Für alle Kapitel nützlich, mit Klang.</p>
    {kachel_liste(WERKZEUGE, "werkzeuge", symbol_key="slug")}
  </section>
</div>
""", beschreibung="Notenlehre für den Musikkurs Klasse 10: Notenwerte, Pausen, Violinschlüssel, Vorzeichen, Dynamik, Tonleitern, Intervalle, Dreiklänge und Quintenzirkel.",
     skripte=JS_NOTEN)
print("fertig:", len(FREI), "Kapitel freigeschaltet")
