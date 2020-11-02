"""
Schreibt eine Funktion, welche ermittelt, mit welchem Schlüssel ein Plaintext
mithilfe der Caesar-Chiffre zu einen verschlüsselten Text umgewandelt wurde.

Beispiel:

calculateSecretKey("banane", "EDQDQH") -> 3
calculateSecretKey("banane", "VUHUHY") -> 20

"""

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


def calculateSecretKey(plainText: str, cipherText: str) -> int:
    for key in range(1, 27):
        decryptedWord = decrypt(cipherText, key)

        if decryptedWord == plainText.upper():
            return key


print(calculateSecretKey("banane", "EDQDQH"))  # 3
print(calculateSecretKey("banane", "VUHUHY"))  # 20
