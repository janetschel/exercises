"""
Schreibt ein Programm, welches anhand des eingegebenen Alters entscheidet,
ob der Benutzer voll- oder minderjährig ist.
"""

ageInput = input("Alter: ")

age = int(ageInput)

if age >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")
