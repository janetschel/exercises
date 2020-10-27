"""
Schreibt eine Funktion, welche die Summe aller Ziffern einer Zahl ermittelt.

Beispiel:
123 -> 6 (1 + 2 + 3 = 6)
1337 -> 14 (1 + 3 + 3 + 7 = 14)

"""


def sumOfDigits(number: int) -> int:
    numberString: str = str(number)
    result: int = 0

    for character in numberString:
        digit: int = int(character)
        result += digit

    return result


print(sumOfDigits(123))  # 6
print(sumOfDigits(1337))  # 14
