"""
Schreibt eine Funktion, welche ermittelt, ob das gesuchte Element in der Liste
enthalten ist.

Beispiel:
[1, 4, 14, 3, 0]
gesuchtes Element 3 -> True
gesuchtes Element 5 -> False
"""


def isElementPresentInList(listInput, element):
    for currentElement in listInput:
        if currentElement == element:
            return True

    return False


listInput = [1, 4, 6, 14, 0]

print(isElementPresentInList(listInput, 4))
