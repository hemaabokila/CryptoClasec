class Caesar:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        """
        Initializes the Caesar cipher with a key.
        Args:
            key (int): The key to be used for the cipher.
        Raises:
            ValueError: If the key is not an integer or is not within a valid range.
        """
        if not isinstance(key, int):
            raise ValueError("The key must be an integer.")
        if key < 0 or key >= len(self.ALPHABET):
            raise ValueError(f"The key must be between 0 and {len(self.ALPHABET) - 1}.")
        self.key = key % 26 

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Caeser cipher.
        Args:
            plaintext (str): The plaintext to encrypt.
        Returns:
            str: The encrypted ciphertext.
        Raises:
            TypeError: If the plaintext is not a string.
        """
        if not isinstance(plaintext, str):
            raise TypeError("The plaintext must be a string.")
        
        ciphertext = ""
        for char in plaintext:
            if char.isalpha(): 
                base = ord("A") if char.isupper() else ord("a")
                cipher = chr((ord(char) - base + self.key) % 26 + base)
                ciphertext += cipher
            else:
                ciphertext += char 
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Caeser cipher.
        Args:
            ciphertext (str): The ciphertext to decrypt.
        Returns:
            str: The decrypted plaintext.
        Raises:
            TypeError: If the ciphertext is not a string.
        """
        if not isinstance(ciphertext, str):
            raise TypeError("The ciphertext must be a string.")
        
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                plain = chr((ord(char) - base - self.key) % 26 + base)
                plaintext += plain
            else:
                plaintext += char  
        return plaintext
