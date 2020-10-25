"""
Schreibt eine for-Schleife, welche jede gerade Zahl bis 100 ausgibt, angefangen bei der 0. Anders könnte man auch sagen, die Schleife
soll jede zweite Zahl ausgeben.
Der Output dieser Schleife sieht demnach so aus:

0
2
4
6
8
...
100

Hinweis: Eine Funktion für das Bearbeiten der Aufgabe ist nicht zwangsweise benötigt.

Sobald ihr fertig seid, schreibt das Gleiche Programm nochmal, allerdings mit einer while-Schleife.
Welche Unterschiede sind an welchen Stellen zu erkennen? Welche Variante würdet ihr bevorzugen und warum?
"""

# Lösung for-Schleife
# Nummer 1
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

# Nummer 2
for i in range(0, 101, 2):
    print(i)


# Lösung while-Schleife
# Nummer 1
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)

    i += 1

# Nummer 2
i = 0
while i <= 100:
    print(i)

    i += 2  # analog zum Step-Parameter in der for-Schleife
