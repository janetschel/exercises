"""

Schreibt eine Funktion, welche ein verschlüsseltes Wort wieder in den Klartext umwandelt.

Beispiel:

decrypt("VUHUHY", 20) -> BANANE
decrypt("EDQDQH", 3) -> BANANE

Der erste Parameter eurer Funktion ist das verschlüsselte

"""

from typing import List


def decrypt(string: str, key: int) -> str:
    decryptedString: str = ""
    for character in string.lower():
        charValue = ord(character)
        decryptedCharacterValue = (charValue - key)
        if decryptedCharacterValue < 97:
            decryptedCharacterValue += 26
        decryptedCharacter = chr(decryptedCharacterValue)
        decryptedString += decryptedCharacter

    return decryptedString.upper()


def decryptSentence(sentence: str, key: int) -> str:
    words: List[str] = sentence.split(" ")
    decryptedWords: List[str] = []

    for word in words:
        decryptedWord = decrypt(word, key)
        decryptedWords.append(decryptedWord)

    return " ".join(decryptedWords)


print(decryptSentence("VUHUHY", 20))
print(decryptSentence("EDQDQH", 3))
