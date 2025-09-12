from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_keygen():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(public_key, plaintext):
    recipient_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    encrypted = cipher.encrypt(plaintext.encode())
    return encrypted

def rsa_decrypt(private_key, ciphertext):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()

# Test RSA
private_key, public_key = rsa_keygen()
plaintext = "This is a secret message."
ciphertext = rsa_encrypt(public_key, plaintext)
decrypted_text = rsa_decrypt(private_key, ciphertext)

print("RSA Encryption")
print("Original:", plaintext)
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:", decrypted_text)


	

