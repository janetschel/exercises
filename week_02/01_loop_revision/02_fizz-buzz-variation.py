"""
Schreibt eine for-Schleife, welche die Zahlen 0 bis 100 (inklusive) durchläuft, und sich folgendermaßen verhält:

- Falls die Zahl durch 4 teilbar ist, gebe "Durch 4 teilbar" auf der Konsole aus
- Falls die Zahl 50 ist, gebe "Wir sind bei der Hälfte" aus
- Falls die Zahl 0 ist, gebe "Start" aus
- Falls nichts der oberen beiden Anforderungen zutrifft, gebe aus: "Das doppelte der Zahl ist <[zahl] * 2>"

Sobald du fertig bist nehmen dir deine for-Schleife und wandel sie in eine while-Schleife um. Was sind hier die Unterschiede?
"""

# for-Schleife
for i in range(0, 101):
    if i == 0:
        print("Start")
    elif i == 50:
        print("Wir sind bei der Hälfte")
    elif i % 4 == 0:
        print("Durch 4 teilbar")
    else:
        print(f"Das doppelte der Zahl ist {i * 2}")


# while-Schleife
i = 0
while i <= 100:
    if i == 0:
        print("Start")
    elif i == 50:
        print("Wir sind bei der Hälfte")
    elif i % 4 == 0:
        print("Durch 4 teilbar")
    else:
        print(f"Das doppelte der Zahl ist {i * 2}")

    i += 1
