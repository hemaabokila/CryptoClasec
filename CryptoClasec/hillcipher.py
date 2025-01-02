class HillCipher:
    def __init__(self, key):
        """
        Initializes the Hill cipher with a key matrix.
        Args:
            key (list): A 2D list representing the key matrix.
        """
        self.key = key
        self.modulus = 26
        if len(self.key) != len(self.key[0]):
            raise ValueError("Key matrix must be square.")

        det = self.determinant(self.key)
        gcd = self.gcd(det, self.modulus)
        if gcd != 1:
            raise ValueError("Key matrix is not invertible. Choose a different key.")
        
        self.inverse_key = self.modular_inverse_matrix(self.key, self.modulus)

    def gcd(self, a, b):
        """Computes the greatest common divisor (GCD) of two numbers."""
        while b:
            a, b = b, a % b
        return a

    def determinant(self, matrix):
        """Computes the determinant of a 2x2 matrix."""
        if len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        raise ValueError("Only 2x2 matrices are supported for determinant.")

    def modular_inverse(self, a, m):
        """
        Computes the modular inverse of a number a modulo m using the extended Euclidean algorithm.
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError(f"No modular inverse for {a} modulo {m}.")

    def modular_inverse_matrix(self, matrix, modulus):
        """
        Computes the modular inverse of a matrix modulo a given modulus.
        Args:
            matrix (list): The input matrix as a list of lists.
            modulus (int): The modulus.
        Returns:
            list: The inverse matrix modulo modulus as a list of lists.
        """
        det = self.determinant(matrix)
        det_inv = self.modular_inverse(det, modulus)
        cofactor_matrix = [
            [matrix[1][1], -matrix[0][1]],
            [-matrix[1][0], matrix[0][0]]
        ]
        
        adjugate_matrix = [[elem % modulus for elem in row] for row in cofactor_matrix]
        return [[(det_inv * adjugate_matrix[i][j]) % modulus for j in range(2)] for i in range(2)]

    def prepare_text(self, text, size):
        """
        Prepares the text for encryption or decryption by dividing it into chunks of a given size.
        Pads with 'X' if necessary.
        """
        text = text.upper().replace(" ", "")
        text = [ord(char) - ord('A') for char in text if char.isalpha()]
        while len(text) % size != 0:
            text.append(ord('X') - ord('A'))
        return text

    def matrix_multiply(self, matrix, vector):
        """Multiplies a matrix with a vector modulo the modulus."""
        return [(sum(matrix[i][j] * vector[j] for j in range(len(matrix[0]))) % self.modulus) for i in range(len(matrix))]

    def encrypt(self, plaintext):
        """
        Encrypts the plaintext using the Hill cipher.
        Args:
            plaintext (str): The plaintext to encrypt.
        Returns:
            str: The encrypted ciphertext.
        """
        prepared_text = self.prepare_text(plaintext, len(self.key))
        ciphertext = []
        for i in range(0, len(prepared_text), len(self.key)):
            chunk = prepared_text[i:i + len(self.key)]
            encrypted_chunk = self.matrix_multiply(self.key, chunk)
            ciphertext.extend(encrypted_chunk)
        return "".join([chr(int(num) + ord('A')) for num in ciphertext])

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext using the Hill cipher.
        Args:
            ciphertext (str): The ciphertext to decrypt.
        Returns:
            str: The decrypted plaintext.
        """
        prepared_text = self.prepare_text(ciphertext, len(self.inverse_key))
        plaintext = []
        for i in range(0, len(prepared_text), len(self.inverse_key)):
            chunk = prepared_text[i:i + len(self.inverse_key)]
            decrypted_chunk = self.matrix_multiply(self.inverse_key, chunk)
            plaintext.extend(decrypted_chunk)
        return "".join([chr(int(num) + ord('A')) for num in plaintext])
