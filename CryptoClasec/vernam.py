class Vernam:
    def __init__(self, key: str):
        """
        Initializes the Vernam cipher with a key.
        Args:
            key (str): The key to be used for the cipher. Should be a non-empty string.
        Raises:
            ValueError: If the key is empty or not a string.
        """
        if not key:
            raise ValueError("Key cannot be empty and must be a string.")
        self.key = key
    
    def _extend_key(self, text_length: int) -> str:
        """
        Extends the key to match the length of the text.
        Args:
            text_length (int): The length of the text to be encrypted or decrypted.
        Returns:
            str: The extended key.
        """
        return (self.key * ((text_length // len(self.key)) + 1))[:text_length]

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Vernam cipher.
        Args:
            plaintext (str): The plaintext to encrypt.
        Returns:
            str: The encrypted ciphertext.
        Raises:
            TypeError: If the plaintext is not a string.
        """
        if not isinstance(plaintext, str):
            raise TypeError("The plaintext must be a string.")
        
        extended_key = self._extend_key(len(plaintext))
        
        cipher_text = ""
        for i in range(len(plaintext)):
            cipher_char = chr(ord(plaintext[i]) ^ ord(extended_key[i]))
            cipher_text += cipher_char
        return cipher_text
    
    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the ciphertext using the Vernam cipher (same as encryption).
        Args:
            cipher_text (str): The ciphertext to decrypt.
        Returns:
            str: The decrypted plaintext.
        Raises:
            TypeError: If the ciphertext is not a string.
        """
        if not isinstance(cipher_text, str):
            raise TypeError("The ciphertext must be a string.")
        return self.encrypt(cipher_text)