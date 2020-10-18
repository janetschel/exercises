"""
Schreibt ein Programm, welches den Umfang und den Flächeninhalt eines
Rechtecks berechnet. Der Benutzer gibt jeweils die Breite und die Höhe an.
"""

widthInput = input("Breite: ")
heightInput = input("Höhe: ")

width = float(widthInput)
height = float(heightInput)

circumference = width * 2 + height * 2
surfaceArea = width * height

print("Umfang: " + str(circumference))
print("Flächeninhalt: " + str(surfaceArea))
