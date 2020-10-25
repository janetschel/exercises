"""
Der Treibstoff für ein Modul an einer Rakete basiert auf dessen Masse.
Genauer gesagt: Um den benötigten Treibstoff für ein Modul an einer Rakete zu berechnen, nimmt man die Masse des Moduls, teilt diese
durch 3, rundet ab und zieht vom Ergebnis 2 ab.

Hier ein paar Beispiele:
- Gegeben ist die Masse 12: 12 / 3 = 4 -> 4 abgerundet bleibt 4 -> 4 - 2 = 2
- Gegeben ist die Masse 14: 14 / 3 = 4,6 -> 4,6 abgerundet ist auch 4, deshalb ist hier der benötigte Treibstoff auch 2
- Gegeben ist die Masse 1969, welche 654 Einheiten Treibstoff benötigt

Um die Rakete erfolgreich starten zu können, muss das Programm die insgesamt benötigte Treibstoffmenge für jedes Modul
(also: für jede "Modul-Masse") ausrechnen und zu einem Gesamtergebnis addieren, damit am Schluss die benötigte Treibstoffmenge für
die gesamte Rakete berechnet wurde.

Beispiel:
Gegeben sind folgenden Modulmassen: [12, 15]
12 / 3 = 4 -> 4 abgerundet bleibt 4 -> 4 - 2 = 2
15 / 3 = 5 -> 5 abgerundet bleibt 5 -> 5 - 2 = 3

2 + 3 = 5
Somit ist die gesamt benötigte Treibstoffmenge für diese Rakete 5

Aufgabe:
Schreibt eine Funktion, welche genau diese Rechnungen durchführt und das Ergebnis zurückgibt.
Verwendet dabei in der Funktion eine der beiden Schleifentypen, die ihr kennt.
Verwendet keine eingebauten Python-Funktionen wie max, len etc.. Wichtig: Verboten ist auch round(...)!
"""

# Input für diese Aufgabe
moduleMasses = [95423, 142796, 88137, 105610, 79299, 110633, 136792, 112578, 75168, 115615, 147584, 72145, 108822, 57753, 96827, 69117, 131220, 111193, 120295, 56240, 111190, 80740, 137267, 113183, 126821, 58966, 63556, 110977, 100328, 75367, 57371, 88235, 134475, 109071, 92653, 73347, 135186, 64534, 81198, 55423, 100060, 149555, 110905, 102826, 129023, 112618, 146542, 102579, 67193]

# Lösung
def calculateNeededFuel(listOfModuleMasses: [int]) -> int:
    neededFuel = 0
    for number in listOfModuleMasses:
        requiredFuelForModule = number // 3 - 2  # oder auch: int(number / 3)
        neededFuel += requiredFuelForModule

    return neededFuel


requiredFuel = calculateNeededFuel(moduleMasses)
print(requiredFuel)
