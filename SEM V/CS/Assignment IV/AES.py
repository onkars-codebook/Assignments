from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv, ct_bytes

def aes_decrypt(iv, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode()

# Test AES
key = get_random_bytes(16)  # AES-128
plaintext = "This is a secret message."
iv, ciphertext = aes_encrypt(plaintext, key)
decrypted_text = aes_decrypt(iv, ciphertext, key)

print("AES Encryption")
print("Original:", plaintext)
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:", decrypted_text)
print()
