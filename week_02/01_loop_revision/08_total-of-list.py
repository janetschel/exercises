"""
Schreibt eine Funktion, welche die Summe einer Liste aus Nummern ermittelt.

Beispiel:
[1, 2, 3] -> 6
[-1, 1, 0] -> 0

"""
from typing import List


def sumOfList(numbers: List[int]) -> int:
    result: int = 0
    for number in numbers:
        result += number

    return result


print(sumOfList([1, 2, 3])) # 6
print(sumOfList([-1, 1, 0])) # 0
