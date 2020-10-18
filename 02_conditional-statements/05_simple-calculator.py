"""
Erstellt ein Programm, welches das Verhalten eines einfachen
Taschenrechners repliziert. Der Benutzer soll nacheinander die erste Zahl,
danach den Operator (+, -, *, /) und zuletzt die zweite Zahl eingeben.

Beispiel:
    1. Zahl: 5
    Operator: *
    2. Zahl: 3

    Ergebnis: 15
"""

firstNumberInput = input("1. Zahl: ")
operatorInput = input("Operator: ")
secondNumberInput = input("2. Zahl: ")

a = int(firstNumberInput)
b = int(secondNumberInput)

result = 0

if operatorInput == "+":
    result = a + b
elif operatorInput == "-":
    result = a - b
elif operatorInput == "*":
    result = a * b
elif operatorInput == "/":
    result = a / b

print("Ergebnis: " + str(result))
