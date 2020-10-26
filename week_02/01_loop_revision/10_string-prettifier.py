"""

Schreibt eine Funktion, welche die Benutzereingabe in einem schönen Rahmen ausgibt.

Beispiel:
"Hello World in a frame"

*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********

"""
from typing import List


def getLengthOfLongestWord(words: List[str]) -> int:
    maxLength: int = 0
    for word in words:
        if len(word) > maxLength:
            maxLength = len(word)

    return maxLength


def prettyPrint(string: str):
    words = string.split(" ")
    lengthOfLongestWord = getLengthOfLongestWord(words)
    print((lengthOfLongestWord + 4) * "*")
    for word in words:
        numberOfRequiredSpaces = lengthOfLongestWord - len(word)
        spaces = numberOfRequiredSpaces * " "
        print(f"* {word}{spaces} *")
    print((lengthOfLongestWord + 4) * "*")


prettyPrint("Hello World in a frame")
