"""
Schreibt eine Funktion, welche eine Nummer in eine Liste bestehend aus den
einzelnen Ziffern umwandelt.

Beispiel:
123 -> [1, 2, 3]
1337 -> [1, 3, 3, 7]

"""
from typing import List


def numberToDigits(number: int) -> List[int]:
    digits: List[int] = []
    numberString: str = str(number)

    for character in numberString:
        digit: int = int(character)
        digits.append(digit)

    return digits


print(numberToDigits(123)) # [1, 2, 3]
print(numberToDigits(1337)) # [1, 2, 3]
