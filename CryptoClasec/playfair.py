class Playfair:
    def __init__(self, key: str):
        """
        Initializes the Playfair cipher with a key.
        Args:
            key (str): The key to be used for the cipher. The key is converted to uppercase and 'J' is replaced with 'I'.
        Raises:
            ValueError: If the key is empty or contains invalid characters.
        """
        if not key:
            raise ValueError("Key cannot be empty.")
        self.key = key.upper().replace("J", "I")
        self.table = self.create_table()

    def create_table(self):
        """
        Creates the Playfair cipher table with the key and remaining letters of the alphabet.
        The table is a 5x5 grid formed from the key and the remaining letters of the alphabet.
        """
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_no_duplicates = "".join(dict.fromkeys(self.key))
        table_string = key_no_duplicates + "".join([c for c in alphabet if c not in key_no_duplicates])
        return [table_string[i:i+5] for i in range(0, 25, 5)]

    def prepare_text(self, text: str) -> list:
        """
        Prepares the text for encryption or decryption by making it uppercase, removing spaces,
        replacing 'J' with 'I', and padding double letters with 'X'.
        """
        text = text.upper().replace("J", "I").replace(" ", "") 
        prepared_text = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared_text.append(text[i] + 'X') 
                i += 1
            else:
                prepared_text.append(text[i] + (text[i + 1] if i + 1 < len(text) else 'X')) 
                i += 2
        return prepared_text

    def find_position(self, letter: str) -> tuple:
        """
        Finds the position of a letter in the Playfair table (row, column).
        """
        for row_idx, row in enumerate(self.table):
            if letter in row:
                return row_idx, row.index(letter)
        return None, None

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the plaintext using the Playfair cipher.
        Args:
            plaintext (str): The plaintext to encrypt.
        Returns:
            str: The encrypted ciphertext.
        Raises:
            TypeError: If the plaintext is not a string.
        """
        if not isinstance(plaintext, str):
            raise TypeError("The plaintext must be a string.")
        
        prepared_text = self.prepare_text(plaintext)
        ciphertext = ""

        for pair in prepared_text:
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            if row1 == row2:
                ciphertext += self.table[row1][(col1 + 1) % 5]
                ciphertext += self.table[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += self.table[(row1 + 1) % 5][col1]
                ciphertext += self.table[(row2 + 1) % 5][col2]
            else:
                ciphertext += self.table[row1][col2]
                ciphertext += self.table[row2][col1]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the ciphertext using the Playfair cipher.
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

        for i in range(0, len(ciphertext), 2):
            pair = ciphertext[i:i+2]
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            if row1 == row2:
                plaintext += self.table[row1][(col1 - 1) % 5]
                plaintext += self.table[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += self.table[(row1 - 1) % 5][col1]
                plaintext += self.table[(row2 - 1) % 5][col2]
            else:
                plaintext += self.table[row1][col2]
                plaintext += self.table[row2][col1]

        return plaintext
