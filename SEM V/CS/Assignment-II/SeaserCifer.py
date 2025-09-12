def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

plain_text = "onkarsathe"
shift = 3
cipher_text = caesar_encrypt(plain_text, shift)
print("Encrypted:", cipher_text)

decrypted = caesar_decrypt(cipher_text, shift)
print("Decrypted:", decrypted)
