"""
Schreibt eine Funktion, welche ermittelt, ob in einer Liste Duplikate
enthalten sind oder nicht.

Beispiel:
[1, 2, 3] -> False
[1, 2, 2, 3] -> True
[1, 2, 1] -> True

"""
from typing import List


def containsDuplicates(list: List[any]) -> bool:
    for element in list:
        if list.count(element) >= 2:
            return True

    return False


print(containsDuplicates([1, 2, 3])) # False
print(containsDuplicates([1, 2, 2, 3])) # True
print(containsDuplicates([1, 2, 1])) # True
