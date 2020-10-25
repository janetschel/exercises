"""
Schreibt ein Programm, welches ermittelt, ob die vom Benutzer eingegebene Zahl
eine Primzahl ist.

Hinweis: Eine Zahl ist nur dann eine Primzahl, wenn sie nur durch 1 oder durch
sich selbst teilbar ist.
"""

userInput = input("Zahl: ")

number: int = int(userInput)

isPrime = True

for i in range(2, number + 1):
    if number % i == 0 and i != number:
        isPrime = False
        break

print("Primzahl" if isPrime else "keine Primzahl")
