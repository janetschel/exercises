"""
Schreibt eine Schleife, welche die Anzahl der Vokale (A, E, I, O, U) in folgendem Satz zählt:

Beautiful is better than ugly. Simple is better than complex. Complex is better than complicated. Readability counts.
If the implementation is hard to explain, it's a bad idea.

Hinweis: Eine Funktion ist hierfür nicht nötig. Wichtig ist die eigene Implementierung
"""

# Diese Zeile am besten auch mit angeben
sentence = "Beautiful is better than ugly. Simple is better than complex. Complex is better than complicated. Readability counts. " \
           "If the implementation is hard to explain, it's a bad idea."

# Lösung
# (der Satz hat 55 Vokale)

vowels = ["a", "e", "i", "o", "u"]
numberOfVowels = 0

for character in sentence.lower():
    if character in vowels:
        numberOfVowels += 1

    # numberOfVowels += 1 if character in vowels else 0

print(numberOfVowels)
