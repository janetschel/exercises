"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Input: 356261, 846303

Ergebnis: 544
"""


def check_adjacent(passcode_str):
    for i in range(len(passcode_str) - 1):
        if passcode_str[i] == passcode_str[i + 1]:
            return True
    return False


def check_ascending_or_equal(passcode_str):
    for i in range(len(passcode_str) - 1):
        if passcode_str[i] > passcode_str[i + 1]:
            return False
    return True


def check_passcode(passcode):
    passcode_str = str(passcode)
    return check_adjacent(passcode_str) and check_ascending_or_equal(passcode_str)


number_of_passcodes = 0

for j in range(356261, 846304):
    if check_passcode(j):
        number_of_passcodes += 1

print(number_of_passcodes)
