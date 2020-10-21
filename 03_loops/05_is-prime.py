"""
Schreibt ein Programm, welches ermittelt, ob die vom Benutzer eingegebene Zahl
eine Primzahl ist.

Hinweis: Eine Zahl ist nur dann eine Primzahl, wenn sie nur durch 1 oder durch
sich selbst teilbar ist.
"""

userInput = input("Zahl: ")

number: int = int(userInput)

isPrime: bool = number > 1

for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

if isPrime:
    print("Primzahl")
else:
    print("Keine Primzahl")
