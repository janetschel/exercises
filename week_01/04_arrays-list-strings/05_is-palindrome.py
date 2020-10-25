"""
Schreibt eine Funktion, welche ermittelt, ob das eingegebene Wort ein Palindrom ist.

Beispiel:
Otto -> True
Peter -> False
"""


def isPalindrome(word):
    lowerCasedWord = word.lower()

    # return lowerCasedWord[::-1] == lowerCasedWord

    length = len(lowerCasedWord)
    for i in range(0, length):
        if lowerCasedWord[i] != lowerCasedWord[length - 1 - i]:
            return False

    return True


print(isPalindrome("Otto"))
print(isPalindrome("Peter"))
