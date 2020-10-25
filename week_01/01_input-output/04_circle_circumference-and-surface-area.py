"""
Schreibt ein Programm, welches den Umfang und den Flächeninhalt eines
Kreises berechnet. Der Benutzer gibt den Radius an.
"""

PI = 3.141592653589793

radiusInput = input("Radius: ")

radius = float(radiusInput)

circumference = 2 * PI * radius
surfaceArea = PI * radius ** 2

print(f"Umfang: {circumference}")
print(f"Flächeninhalt: {surfaceArea}")
