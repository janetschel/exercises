"""
Schreibt ein Programm, welches nur Alice und Bob grüßt, ansonsten soll
"Dich kenne ich nicht" ausgegeben werden. Der Benutzer gibt den Namen ein.

Beispiel:
Eingabe "Bob" -> "Hallo, Bob!"
Eingabe "Peter" -> "Dich kenne ich nicht!"
"""

nameInput = input("Name: ")

if nameInput.lower() == "alice":
    print("Hallo, Alice!")
elif nameInput.lower() == "bob":
    print("Hallo, Bob!")
else:
    print("Dich kenne ich nicht.")
