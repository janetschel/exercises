"""
Schreibt ein Programm, welches durch die Zahlen von 1 bis 100 iteriert.
Wenn die Zahl durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben
werden. Ist die Zahl durch 5 teilbar, soll "Buzz" ausgegeben werden.
Sonderfall: Wenn die Zahl durch 3 und 5 teilbar ist, soll "FizzBuzz" ausgegeben
werden.

Beispiel:
    1:
    2:
    3: Fizz
    4:
    5: Buzz
    6: Fizz
    ...
    15: FizzBuzz
    ...
    100: Buzz
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(f"{i}:")
