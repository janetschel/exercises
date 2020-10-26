"""
Schreibt eine Funktion, welche die Zahlen zwischen 0 und einer eingegebenen Zahl (inklusive) addiert, und das Ergebnis zurückgibt.
Benutzt zur Lösung dieser Aufgabe eine der beiden Schleifentypen.

Hinweis: achtet bei dieser Aufgabe auf Type-Hintings

Zusatzaufgabe:
Gibt es eine charmantere Lösung, bei der keine Schleife benötigt wird? Falls ja, implementiere sie!
"""

# Lösung
def calculateSum(number: int) -> int:
    result = 0
    for i in range(1, number + 1):
        result += i

    return result


sumOfCountingNumbersTo100 = calculateSum(100)
print(sumOfCountingNumbersTo100)


# Elegantere Lösung nach gaußscher Summenformel (https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Summenformel)
# Die Summenformel sollte jeder TN durch eine einfache Google-Suche finden
def calculateSumAdvanced(number: int) -> int:
    return (number * (number + 1)) // 2


sumOfCountingNumbersTo100Advanced = calculateSumAdvanced(100)
print(sumOfCountingNumbersTo100Advanced)


# Überprüft, ob beide Lösungen equivalent sind (Spoiler: ja, sind sie...)
print(calculateSum(100) == calculateSumAdvanced(100))
print(calculateSum(500) == calculateSumAdvanced(500))
print(calculateSum(950) == calculateSumAdvanced(950))
print(calculateSum(1000) == calculateSumAdvanced(1000))
