"""
Schreibt ein Programm, welches die Summe aller Zahlen von 1 bis zu der
Zahl berechnet, die der Benutzer eingegeben hat.
Für die Lösung beide Varianten (for- und while-Schleife) implementieren!
"""

userInput: str = input("Zahl: ")

number: int = int(userInput)

result: int = 0

for n in range(1, number + 1):
    result += n

# i: int = 1
# while i <= number:
#     result += i
#     i += 1

print(f"Die Summe aller Zahlen von 1 bis {userInput} ist: {result}")
