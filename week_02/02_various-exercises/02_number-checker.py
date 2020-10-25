"""
Schreibt ein Programm, welches eine von einem User eingegebene Zahl auf ihre Richtigkeit hin überprüft.

Eine Zahl ist richtig - oder auch valide - wenn sie ALLE folgenden Kriterien erfüllt:
- Die Zahl muss 6-stellig sein
- Die Zahl muss von links nach rechts aufsteigend in seinen Ziffern sortiert sein
- Die Zahl muss mindestens eine Ziffer mindestens doppelt enthalten

Generell kann man also sagen: die Zahl muss eine 6-stellige Zahl sein, bei welcher eine Ziffer nie kleiner sein darf, als ihr Vorgänger
und welche mindestens eine der Ziffern doppelt einhalten muss

Beispiele:
- Die Zahl 123456 ist nicht valide. Sie ist zwar 6-stellig und ihre Ziffern sind aufsteigend sortiert, allerdings enthält sie keine
  Ziffer doppelt
- Die Zahl 112376 ist nicht valide. Sie ist zwar 6-stellig und hat mindestens eine Ziffer doppelt, allerdings ist sie nicht aufsteigend
  sortiert. Das Problem hier die 6, welche auf die 7 folgt (6 kleiner 7, nicht aufsteigend sortiert)
- Die Zahl 445799 ist valide. Sie ist 6-stellig, hat mindestens eine Zahl, welche mindestens doppelt vorkommt und ist aufsteigend
  geordnet.
- Die Zahl 111111 ist auch valide. Sie ist 6-stellig und hat mindestens eine Zahl welche MINDESTENS doppelt vorkommt

Aufgabe:
Schreibt ein Programm, welches den User um eine Eingabe bittet, und diese Zahl mithilfe einer Funktion auf ihre Validität überprüft.
Die Funktion soll als Parameter den User-Input erhalten und True (falls Input valide) oder False (falls nicht) zurückgeben.
Benutzt in der Lösung nicht die len(...) Funktion von Python!

Hinweis/Tipp: Ist es sinnvoll, den Input vom User direkt in ein int umzuwandeln, oder arbeitet man lieber etwas mit dem string?
"""

# Lösung
def checkNumber(inputNumber: str) -> bool:
    hasDoubleDigits: bool = False
    numberOfDigits: int = 1  # muss bei 1 starten, da der Schleifendurchlauf bei len - 1 endet (1 char wird durch L42 nicht gezählt)

    for i in range(0, len(inputNumber) - 1):
        currentNumber: int = int(inputNumber[i])
        nextNumber: int = int(inputNumber[i + 1])

        if currentNumber > nextNumber:
            return False
        elif currentNumber == nextNumber:
            hasDoubleDigits = True

        numberOfDigits += 1

    return hasDoubleDigits and numberOfDigits == 6


inputFromUser: str = input("Welche Zahl soll auf Validität überprüft werden?: ")
print(checkNumber(inputFromUser))
