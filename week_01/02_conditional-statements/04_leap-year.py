"""
Schreibt ein Programm, welches ermittelt, ob die eingegebene Zahl ein
Schaltjahr ist.
Die Eigenschaften für ein Schaltjahr lauten wie folgt:
  1. Das Jahr ist durch 4 teilbar
  2. Wenn das Jahr durch 100 teilbar ist, dann ist es KEIN Schaltjahr
  3. Wenn das Jahr allerdings durch 400 teilbar ist, dann ist es doch ein Schaltjahr

Anders formuliert:
Ein Jahr ist ein Schaltjahr, wenn es...
durch 4 teilbar ist und nicht durch 100 teilbar ist oder durch 400 teilbar ist
"""

yearInput = input("Jahr: ")

year = int(yearInput)

isLeapYear = False

if year % 4 == 0:
    isLeapYear = True
if year % 100 == 0:
    isLeapYear = False
if year % 400 == 0:
    isLeapYear = True

# Alternative:
# isLeapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if isLeapYear:
    print(f"{yearInput} ist ein Schaltjahr.")
else:
    print(f"{yearInput} ist kein Schaltjahr.")
