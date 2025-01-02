# Cryptography Library
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

A Python library for implementing and working with various classical encryption algorithms. This library provides a collection of ciphers that you can use to encrypt and decrypt data in educational or practical cryptography-related projects.

---

## Features
This library includes the following classical ciphers:
- **Caesar Cipher**: A substitution cipher that shifts letters by a fixed number.
- **Monoalphabetic Cipher**: A substitution cipher where each character is replaced by another character using a key.
- **Vigenere Cipher**: A polyalphabetic substitution cipher that uses a keyword to encrypt data.
- **Vernam Cipher**: A stream cipher that uses a key of the same length as the plaintext for encryption.
- **Playfair Cipher**: A digraph substitution cipher that encrypts pairs of letters.
- **Hill Cipher**: A cipher based on linear algebra that uses matrix multiplication for encryption.

---

## Installation
You can install this library using `pip`:

```bash
pip install CryptoClasec
```
## Usage
Here’s how to use the library in your Python project:

### Import the Cipher Classes
```bash
from CryptoClasec import Caesar, Monoalphabetic, Vigenere, Vernam, Playfair, HillCipher
```
### Example: Caesar Cipher
```python
# Initialize the Caesar cipher with a shift value of 3
caesar = Caesar(3)

# Encrypt a plaintext
encrypted = caesar.encrypt("HELLO")
print("Encrypted text:", encrypted)

# Decrypt the ciphertext
decrypted = caesar.decrypt(encrypted)
print("Decrypted text:", decrypted)
```
### Example: Vigenere Cipher
```python
# Initialize the Vigenere cipher with a keyword
vigenere = Vigenere("KEY")

# Encrypt a plaintext
encrypted = vigenere.encrypt("HELLO")
print("Encrypted text:", encrypted)

# Decrypt the ciphertext
decrypted = vigenere.decrypt(encrypted)
print("Decrypted text:", decrypted)
```
## Available Classes
1- Caesar:
```python
caesar = Caesar(3)
caesar.encrypt(plaintext)
caesar.decrypt(ciphertext)
```
2- Monoalphabetic:
```python
mono = Monoalphabetic("QWERTYUIOPLKJHGFDSAZXCVBNM")
mono.encrypt(plaintext)
mono.decrypt(ciphertext)

```
2- Vigenere:
```python
vigenere = Vigenere("KEY")
vigenere.encrypt(plaintext)
vigenere.decrypt(ciphertext)
```
4- Vernam:
```python
vernam = Vernam("RANDOMKEY")
vernam.encrypt(plaintext)
vernam.decrypt(ciphertext)
```
5- Playfair:
```python
playfair = Playfair("KEYWORD")
playfair.encrypt(plaintext)
playfair.decrypt(ciphertext)
```
6- HillCipher:
```python
hill = HillCipher([[2, 3], [1, 4]])
hill.encrypt(plaintext)
hill.decrypt(ciphertext)
```
## License
This library is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the library.
## Author
Created by Ibrahem abo kila. For any inquiries, please contact me at ibrahemabokila@gmail.com.
