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

replay = "y"

print("In wievielen Versuchen kannst du eine Zahl zwischen 1 und 100 erraten?")

while replay == "y":
    randomNumber = random.randint(1, 100)
    numberOfGuesses = 0

    while True: #Use do-while if possible
        guessedNumber = int(input("An welche Zahl denke ich? "))
        numberOfGuesses += 1

        if guessedNumber == randomNumber:
            print(f"Korrekt! Du hast {numberOfGuesses} Versuche gebraucht.")
            break
        else:
            print(f"Meine Zahl ist {'größer' if guessedNumber < randomNumber else 'kleiner'} als {guessedNumber}.")

    replay = input("Möchtest du nochmal spielen? (y/n) ")