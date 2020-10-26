"""

Schreibt eine Funktion, welche die Länge des längsten Wortes eines Satzes zurückgibt.

Beispiel:
"The quick brown fox jumps over the lazy dog" -> 5
"Eine Banane ist nicht immer krumm" -> 6

"""
from typing import List


def getLengthOfLongestWord(string: str) -> int:
    words: List[str] = string.split(" ")
    maxLength: int = 0
    for word in words:
        if len(word) > maxLength:
            maxLength = len(word)

    return maxLength


print(getLengthOfLongestWord("The quick brown fox jumps over the lazy dog")) # 5
print(getLengthOfLongestWord("Eine Banane ist nicht immer krumm")) # 6
