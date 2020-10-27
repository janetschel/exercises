"""
Schreibt eine Funktion, welche ganze Sätze mithilfe der Caesar-Verschlüsselung verschlüsselt.
(siehe https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung)
Für die Verschlüsselung soll der Schlüssel 3 verwendet werden.

Beispiel:
The quick brown fox jumps over the lazy dog -> WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ

"""
from typing import List


def encrypt(string: str) -> str:
    encryptedString: str = ""
    for character in string.lower():
        charValue = ord(character)
        encryptedCharValue = (charValue + 3)
        if encryptedCharValue > 122:
            encryptedCharValue -= 26
        encryptedCharacter = chr(encryptedCharValue)
        encryptedString += encryptedCharacter

    return encryptedString.upper()


def encryptSentence(sentence: str) -> str:
    words: List[str] = sentence.split(" ")
    encryptedWords: List[str] = []

    for word in words:
        encryptedWord = encrypt(word)
        encryptedWords.append(encryptedWord)

    return " ".join(encryptedWords)


print(encryptSentence("The quick brown fox jumps over the lazy dog"))
# WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
