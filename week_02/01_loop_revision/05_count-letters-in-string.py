"""
Schreibt eine Funktion, welche die Anzahl der Zeichen (Leerzeichen AUSGENOMMEN) in einem beliebigen String
zählt, und dem Benutzer im folgenden Format ausgibt: "In deinem Satz sind <anzahl> Zeichen enthalten".

Hallo, Welt -> 10
Hallo -> 5
Ha Llo -> 5
H a l l o -> 5

Hinweis:
- Benutzt hierbei NICHT die eingebauten Funktion len(str) oder andere Hilfsmethoden!
  Gefordert ist sozusagen eine eigene Implementation dieser Methode, welche Leerzeichen ignoriert.
- Type-Hinting im Methodenkopf ist bei dieser Aufgabe nicht notwendig

Tipp: Überlege gut: gibt es hierbei eine Schleife, welche definitiv zu bevorzugen ist?
"""

# Lösung
def countLettersInString(string):
    numberOfCharsInString = 0

    for char in string:
        if char != ' ':
            numberOfCharsInString += 1

    print(f"In deinem Satz sind {numberOfCharsInString} Zeichen enthalten")


inputFromUser = input("Satz: ")
countLettersInString(inputFromUser)
