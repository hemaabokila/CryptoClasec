class Monoalphabetic:
    def __init__(self, key: str):
        """
        Initializes the Monoalphabetic cipher with a key.
        Args:
            key (str): A 26-letter string representing the substitution key.
        Raises:
            ValueError: If the key does not contain all unique letters.
        """
        if len(key) != 26 or len(set(key.lower())) != 26:
            raise ValueError("Invalid key: Key must contain all 26 unique letters.")
        self.key = key.lower()
        self.encrypt_dict = {chr(i + 97): self.key[i] for i in range(26)}
        self.decrypt_dict = {self.key[i]: chr(i + 97) for i in range(26)}
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Monoalphabetic cipher.
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
                is_upper = char.isupper()
                char = char.lower()
                cipher = self.encrypt_dict[char]
                ciphertext += cipher.upper() if is_upper else cipher
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Monoalphabetic cipher.
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
                is_upper = char.isupper()
                char = char.lower()
                plain = self.decrypt_dict[char]
                plaintext += plain.upper() if is_upper else plain
            else:
                plaintext += char 
        return plaintext
