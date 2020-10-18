"""
Schreibt ein Programm, welches dem Nutzer nacheinander die drei Farben
rot, gelb und blau auswählen lässt. Die Auswahl erfolgt über die Eingabe von
0 (= Farbe nicht verwenden) und 1 (= Farbe zum Mischen verwenden).
Anschließend soll die resultierende Farbe ausgegeben werden.

Beispiel:
    rot: 1
    gelb: 0
    blau: 1

    Ausgabe: "Die Resultierende Farbe ist: lila"
"""

redInput = input("Rot: ")
yellowInput = input("Gelb: ")
blueInput = input("Blau: ")

red = bool(int(redInput))
yellow = bool(int(yellowInput))
blue = bool(int(blueInput))

result: str = ""

if red and yellow and blue:
    result = "weiß"
elif red and yellow and not blue:
    result = "orange"
elif red and not yellow and blue:
    result = "lila"
elif not red and yellow and blue:
    result = "grün"
elif red and not yellow and not blue:
    result = "rot"
elif not red and yellow and not blue:
    result = "gelb"
elif not red and not yellow and blue:
    result = "blue"
else:
    result = "Fehler"

print("Die resultierende Farbe ist: " + result)
