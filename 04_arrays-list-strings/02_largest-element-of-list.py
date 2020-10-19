"""
Schreibt eine Funktion, welche das größte Element einer Liste zurückgibt.

Beispiel:
[1, 4, 14, 3, 0] -> 14
"""

def findBiggestElementInList(listInput):
    # return max(listInput)

    biggestElement = None
    for element in listInput:
        if biggestElement is None or element > biggestElement:
            biggestElement = element

    return biggestElement


listInput = [1, 4, 14, 3, 0]
biggestElementPresentInList = findBiggestElementInList(listInput)

print(biggestElementPresentInList)
