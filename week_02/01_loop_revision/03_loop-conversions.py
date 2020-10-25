"""
Schreibt folgende for-Schleifen in while-Schleifen um.

Welche Unterschiede sind zu finden, und welche Elemente von der for-Schleife sind wo in einer while-Schleife zu finden.
Sind for-Schleifen generell besser?
"""

# Schleife 1
for i in range(0, 50, 5):
    print(i)


# Schleife 2
for i in range(50, -1, -2):
    print(i)


# Schleife 3
listInput = [5, 412, 655, 25, 968]

for number in listInput:
    if number % 5 == 0:
        print(number)


# ---------------------------------
# Lösungen

# Schleife 1
i = 0
while i < 50:  # oder i <= 49
    print(i)
    i += 5


# Schleife 2
i = 50
while i >= 0:  # oder i < -1
    print(i)
    i -= 2


# Schleife 3
listInput = [5, 412, 655, 25, 968]

i = 0
listLength = len(listInput)

while i < listLength:
    number = listInput[i]

    if number % 5 == 0:
        print(number)
