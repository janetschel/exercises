"""
Schreibt eine Funktion, welche ermittelt, mit welchem Schlüssel ein Plaintext
mithilfe der Caesar-Chiffre zu einen verschlüsselten Text umgewandelt wurde.

Beispiel:

calculateSecretKey("banane", "EDQDQH") -> 3
calculateSecretKey("banane", "VUHUHY") -> 20

"""


def calculateSecretKey(plainText: str, cipherText: str) -> int:
    secretKey: int = -1

    # TODO: implement

    return secretKey


print(calculateSecretKey("banane", "EDQDQH"))  # 3
print(calculateSecretKey("banane", "VUHUHY"))  # 20
