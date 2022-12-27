from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

BS = DES3.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt(plaintext, key):
    plaintext = pad(plaintext)
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext

def decrypt(ciphertext, key):
#    plaintext = ciphertext.decode('utf-8')
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext)
    plaintext.decode('utf-8')
    return plaintext


key = get_random_bytes(16)
print(f'Ключ: {key}')
while True:
    print('Выберите:\n\t1 - Зашифровать\n\t2 - Расшифровать')
    operation = input('Ваш выбор: ')
    if operation == '1':
        plaintext = input("Введите строку: ")
        print(encrypt(plaintext, key))
    if operation == '2':
        ciphertext = input("Введите строку: ")
        print(decrypt(ciphertext, key))
