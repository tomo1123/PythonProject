import os

from Crypto.Cipher import AES

# キーとIVをランダムなバイト列として生成
key = os.urandom(AES.block_size)
iv = os.urandom(AES.block_size)

def pad(s):
    padding_length = AES.block_size - len(s) % AES.block_size
    padding = bytes([padding_length] * padding_length)
    return s + padding


def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext)
    return cipher.encrypt(padded_text)

with open('plaintext.txt', 'r') as f, open('enc.dat', 'wb') as e:
    plaintext = f.read()
    cipher_text = encrypt(plaintext, key, iv)
    e.write(cipher_text)
