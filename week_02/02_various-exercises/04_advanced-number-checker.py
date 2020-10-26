"""
Benutzt eure Funktion aus der Lösung der vorherigen Aufgabe (03_number-checker.py) um diese Aufgabe zu lösen.

Aufgabe:
Wie viele valide Zahlen gibt es zwischen 111111 und 999999 (inklusive)?

Tipp: falls ihr auf die Lösung zu lange wartet kann es sein, dass diese zu unperformant ist. Überprüft in diesem Fall eure
Lösung und schaut, an welcher Stelle ihr Zeit sparen könnt.

Hinweis: die durchschnittliche Execution-Time der Musterlösung pro Durchlauf (gemessen an 50 Durchläufen) ist: 1.3s
"""

# Lösung
# (Anzahl valider Nummern: 2919)

# Funktion aus 03_number-checker.py. Diese Funktion kann leider nicht importiert werden, da die file-namings zu Syntax-Errors führen
def checkNumber(inputNumber: str) -> bool:
    hasDoubleDigits: bool = False
    numberOfDigits: int = 1

    for i in range(0, len(inputNumber) - 1):
        currentNumber: int = int(inputNumber[i])
        nextNumber: int = int(inputNumber[i + 1])

        if currentNumber > nextNumber:
            return False
        elif currentNumber == nextNumber:
            hasDoubleDigits = True

        numberOfDigits += 1

    return hasDoubleDigits and numberOfDigits == 6


sumOfValidNumbers = 0
for i in range(111111, 999999 + 1):  # +1 da stop exklusive behandelt wird
    isValidNumber = checkNumber(str(i))

    if isValidNumber:
        sumOfValidNumbers += 1

print(sumOfValidNumbers)
