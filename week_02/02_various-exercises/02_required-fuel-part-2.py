"""
Bei der ersten Teilaufgabe haben wir nun also berechnet, wie viel Treibstoff jedes einzelne Modul benötigt.
Allerdings haben wir hierbei etwas Wichtiges vergessen: Treibstoff wiegt selber auch etwas.

Das heißt auf gut Deutsch:
Die Masse von Treibstoff braucht auch wieder Treibstoff, dieser Treibstoff braucht auch wiederrum Treib-
stoff, und so weiter. Die Rechnung, um den benötigten Treibstoff von Treibstoff zu berechnen, ist genau die Gleiche, als wenn ich
den Treibstoffbedarf eines Moduls ausrechne: durch 3 dividieren, abrunden, und 2 abziehen.
Jede Masse, welche negativen Treibstoffbedarf hätte, wird betrachetet, als hätte es keinen (0) Treibstoffbedarf.

Das heißt: für jedes Modul muss zunächst die benötigte Treibstoffmenge berechnet und zum Gesamtergebnis addiert werden. Danach muss
die Treibstoffmenge dieser Treibstoffmenge berechnet werden, und so weiter.

Beispiel:
- Wir haben eine Modulmasse von 14 gegeben. 14 / 3 = 4,6 -> 4,6 abgerunden ist 4 -> 4 - 2 ist 2.
- Diese Treibstoffmenge von 2 braucht auch wieder Treibstoff: 2 / 3 = 0,67 -> 0,67 abgerundet ist 0. Somit brauchen wir hier keinen
  weiteren Treibstoff (da 0 - 2 = -2, was negativ ist -> 0)

- Wir haben eine Modulmasse von 1969, welche zunächst 654 Einheiten Treibstoff benötigt.
- Diese 654 Treibstoff-Einheiten benötigen weitere 216 Einheiten (654 / 3 = 218 -> 218 - 2 = 216)
- 216 braucht noch 70 Treibstoffeinheiten, welche 21 benötigen, welche 5 benötigen. 5 braucht keinen weiteren Treibstoff.
- Somit ist dann der gesamte Treibstoffbedarf für die Modulmasse 1969 966 (654 + 216 + 70 + 21 + 5 = 966)

- Der benötigte Treibstoff für die Modulmasse 100756 ust 50346

Beispiel:
Gegeben sind die Modulmassen: [12, 15, 100]
- 12: 12 / 3 = 4 -> 4 abgerundet ist 4 -> 4 - 2 = 2 --> 2 / 3 = 0,67 -> 0,67 abgerundet ist 0 -> 0 - 2 = -2 -> 0, da negative
  Treibstoffmengen immer als 0 behandelt werden sollen. Somit ist die benötigte Treibstoffmenge für die Modulmasse 12 insgesamt
  2 (2 + 0 = 2)
- 15: 15 / 3 = 5 -> 5 - 2 = 3 --> 3 / 3 = 1 -> 2 - 1 = -1 -> 0, somit ist die gesamte Treibstoffmenge für die Modulmasse 15 insgesamt
  3 (3 + 0 = 3)
- 100: 100 / 3 = 33,34 -> 33,34 abgerundet sind 33 -> 33 - 2 = 31 --> 31 / 3 = 10,34 -> 10,34 abgerundet sind 10 -> 10 - 2 = 8
  --> 8 / 3 = 2,67 -> 2,67 abgerundet sind 2 -> 2 - 2 = 0
  Somit ist die Treibstoffmenge für die Modulmasse insgesamt 39 (31 + 8 + 0 = 39)

Aufgabe:
Schreibt eine Funktion, welche die insgesamte Treibstoffmenge nach diesen Kriterien berechnet und diese zurückgibt.
Benutze für die Lösung der Aufgabe den gleichen Input von der ersten Aufgabe, und berechne die insgesamt benötigte Treibstoffmenge,
wenn der Treibstoff auch Treibstoff braucht.
"""

# Input für diese Aufgabe
moduleMasses = [95423, 142796, 88137, 105610, 79299, 110633, 136792, 112578, 75168, 115615, 147584, 72145, 108822, 57753, 96827, 69117, 131220, 111193, 120295, 56240, 111190, 80740, 137267, 113183, 126821, 58966, 63556, 110977, 100328, 75367, 57371, 88235, 134475, 109071, 92653, 73347, 135186, 64534, 81198, 55423, 100060, 149555, 110905, 102826, 129023, 112618, 146542, 102579, 67193]

# Mit Schleife
def calculateNeededFuel(listOfModuleMasses: [int]) -> int:
    neededFuel = 0

    for moduleMass in listOfModuleMasses:
        neededFuelForModule = 0
        currentRequiredFuel = moduleMass

        while currentRequiredFuel > 2:  # Das ist die letzte valide Zahl, bei der x - 2 nicht negativ oder 0ist
            requiredFuel = currentRequiredFuel // 3 - 2
            currentRequiredFuel = requiredFuel

            neededFuelForModule += requiredFuel

        neededFuel += neededFuelForModule

    return neededFuel


requiredFuel = calculateNeededFuel([100756])
print(requiredFuel)
