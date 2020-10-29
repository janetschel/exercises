"""
Schreibt eine Funktion, welche die Summe aller Ziffern einer Zahl ermittelt.

Beispiel:
123 -> 6 (1 + 2 + 3 = 6)
1337 -> 14 (1 + 3 + 3 + 7 = 14)

"""


def calculateSumOfDigits(number: int) -> int:
    numberString: str = str(number)
    sumOfDigits: int = 0

    for character in numberString:
        digit: int = int(character)
        sumOfDigits += digit

    return sumOfDigits


print(calculateSumOfDigits(123))  # 6
print(calculateSumOfDigits(1337))  # 14
