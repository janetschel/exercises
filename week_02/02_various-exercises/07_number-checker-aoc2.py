"""
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""


def check_valid_number_of_equals(str_to_count):
    for x in range(10):
        number_of_occurences = 0
        for letter in str_to_count:
            if letter == str(x):
                number_of_occurences += 1
        if number_of_occurences == 2:
            return True
    return False


def check_ascending_or_equal(passcode_str):
    for i in range(len(passcode_str) - 1):
        if passcode_str[i] > passcode_str[i + 1]:
            return False
    return True


def check_passcode(passcode):
    passcode_str = str(passcode)
    return check_ascending_or_equal(passcode_str) and check_valid_number_of_equals(passcode_str)


number_of_passcodes = 0

for j in range(356261, 846304):
    if check_passcode(j):
        number_of_passcodes += 1

print(number_of_passcodes)
