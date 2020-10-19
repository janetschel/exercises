"""
Schreibt ein Programm, welches ausgibt, ob die eingegebene Zahl durch 2
teilbar ist.
"""

numberInput = input("Zahl: ")

number = int(numberInput)

if number % 2 == 0:
    print(f"Die Zahl '{numberInput}' ist durch 2 teilbar.")
else:
    print(f"Die Zahl '{numberInput}' ist nicht durch 2 teilbar.")
