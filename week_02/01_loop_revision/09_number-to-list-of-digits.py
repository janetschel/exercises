"""
Schreibt eine Funktion, welche eine Nummer in eine Liste bestehend aus den
einzelnen Ziffern umwandelt.

Beispiel:
123 -> [1, 2, 3]
1337 -> [1, 3, 3, 7]

"""
from typing import List


def numberToDigits(number: int) -> List[int]:
    result: List[int] = []
    numberString: str = str(number)

    for character in numberString:
        digit: int = int(character)
        result.append(digit)

    return result


print(numberToDigits(123)) # [1, 2, 3]
print(numberToDigits(1337)) # [1, 2, 3]
