"""
Schreibt ein Programm, welches die Anzahl der Zeichen und Zahlen in den Eingabe
des Benutzers zählt und wieder ausgibt.

Achtung: Leerzeichen sollen nicht zu der Anzahl der Zeichen gerechnet werden!
"""

userInput: str = input("Gebe hier deinen Satz ein: ")

numberOfDigits = 0
numberOfCharacters = 0

for character in userInput:
    if character.isdigit():
        numberOfDigits += 1
    elif character.isalpha() and character != " ":
        numberOfCharacters += 1

print("Zeichen: " + str(numberOfCharacters))
print("Zahlen: " + str(numberOfDigits))
