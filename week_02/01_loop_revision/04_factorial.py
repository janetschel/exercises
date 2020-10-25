"""
Schreibt eine Funktion, welche die Fakultät einer eingegeben Zahl (Parameter der Funktion) berechnet und zurückgibt.

Die Fakultät einer Zahl z ist folgendermaßen definiert:
z! = z * (z - 1) * (z - 2) * ... * 3 * 2 * 1

Das heißt auf gut Deutsch:
6! = 6 * (6 - 1) * (6 - 2) * 3 * 2 * 1 = 720
                             ^
                          (6 - 3)

5! = 5 * 4 * 3 * 2 * 1 = 120
3! = 3 * 2 * 1 = 6
2! = 2 * 1 = 2
1! = 1

Bei der Berechnung der Fakultät werden von der ausgehenden Zahl also alle Zahlen bis 1 (inklusive) miteinander multipliziert.
Benutzt für die Lösung innerhalb der Funktion eine der beiden Schleifentypen.

Tipp: der Methodenkopf der Funktion sieht demnach folgendermaßen aus:
def calculateFactorial(number: int) -> int:
    # ...

Bzw. ohne Typ-Hinting:
def calculateFactorial(number):
    # ...
"""

# Lösung
def calculateFactorial(number: int) -> int:
    result = number

    for currentNumber in range(number - 1, 0, -1):
        result *= currentNumber

    # currentNumber = number - 1
    # while currentNumber > 0:
    #     result *= currentNumber
    #     currentNumber -= 1

    return result


inputFromUser: str = input("Für welche Zahl soll die Fakultät berechnet werden?: ")
inputNumber: int = int(inputFromUser)

factorialOfNumber = calculateFactorial(inputNumber)
print(factorialOfNumber)
