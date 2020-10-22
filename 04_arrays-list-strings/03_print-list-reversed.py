"""
Schreibt eine Funktion, welche alle Elemente in umgekehrter Reihenfolge ausgibt.

Beispiel:
[1, 4, 14, 3, 0] -> 0 3 14 4 1
"""


def reverseList(listInput):
    for element in listInput[::-1]:
        print(element)

    # for i in range(len(listInput) - 1, -1, -1):
    #     print(listInput[i])


reverseList([1, 4, 14, 3, 0])
