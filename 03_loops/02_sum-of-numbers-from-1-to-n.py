"""
Schreibt ein Programm, welches die Summe aller Zahlen von 1 bis zu der
Zahl berechnet, die der Benutzer eingegeben hat.
Für die Lösung beide Varianten (for- und while-Schleife) implementieren!
"""

userInput = input("Zahl: ")

number = int(userInput)

result: int = 0

for n in range(1, number + 1):
    result += n

print(f"Die Summe aller Zahlen von 1 bis {userInput} ist: {result}")
