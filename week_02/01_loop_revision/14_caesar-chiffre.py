"""
Schreibt eine Funktion, welche ein Wort mithilfe der Caesar-Verschlüsselung verschlüsselt.
(siehe https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung)
Für die Verschlüsselung soll der Schlüssel 3 verwendet werden.

Beispiel:

Banane -> EDQDQH
Zahnarzt -> CDKQDUCW

"""


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


print(encrypt("Banane"))  # EDQDQH
print(encrypt("Zahnarzt"))  # CDKQDUCW
