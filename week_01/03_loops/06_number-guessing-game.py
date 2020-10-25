"""
Schreibt ein Programm, welches folgendermaßen funktioniert:

Der Computer bestimmt durch Zufall einer Zahl zwischen 1 und 100.
Der Benutzer soll versuchen, diese Zahl zu erraten.
Ist die Zahl zu groß, wird "deine gerate Zahl ist zu groß" ausgegeben.
Ist die Zahl zu klein, wird "deine gerate Zahl ist zu klein" ausgegeben.
Hat der Benutzer die richtige Zahl erraten, soll "Gewonnen" und die Anzahl der
Versuche ausgegeben werden.
"""

import random

print("In wie vielen Versuchen kannst du eine Zahl zwischen 1 und 100 erraten?")

randomNumber: int = random.randint(1, 100)
guessedNumber: int = -1
numberOfGuesses: int = 0

while guessedNumber != randomNumber:
    guessedNumber = int(input("An welche Zahl denke ich? "))
    numberOfGuesses += 1

    if guessedNumber < randomNumber:
        print(f"Meine Zahl ist größer als {guessedNumber}")
    elif guessedNumber > randomNumber:
        print(f"Meine Zahl ist kleiner als {guessedNumber}")
    else:
        print(f"Korrekt! Du hast {numberOfGuesses} Versuche gebraucht.")
