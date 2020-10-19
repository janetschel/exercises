"""
Schreibt ein Programm, welches die Multiplikationstabelle von 1 bis 12 ausgibt.

Beispiel:
1 x 1 = 1
1 x 2 = 2
...
12 x 11 = 132
12 x 12 = 144

Verwendet die Schleifen-Variante, welche euch lieber ist.
"""

for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")
