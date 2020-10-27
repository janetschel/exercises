"""
Schreibt eine Funktion, welche ermittelt, ob zwei Arrays gleich sind
(unabhängig von den enthaltenen Datentypen!)

Beispiel:

isEqual([1, 2, 3], [1, 2, 3]) -> True
isEqual([1, 2, 3], [1, 2]) -> False
isEqual([1, 2, 3], [3, 3, 3]) -> False
isEqual([1, 2, 3], [3, 2, 1]) -> False
isEqual(["Hans", "Laura"], ["Hans", "Laura"]) -> True

"""
from typing import List


def isEqual(list1: List[any], list2: List[any]) -> bool:
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


print(isEqual([1, 2, 3], [1, 2, 3]))  # True
print(isEqual([1, 2, 3], [1, 2]))  # False
print(isEqual([1, 2, 3], [3, 3, 3]))  # False
print(isEqual([1, 2, 3], [3, 2, 1]))  # False
print(isEqual(["Hans", "Laura"], ["Hans", "Laura"]))  # True
