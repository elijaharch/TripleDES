from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64
import random
import string

BS = DES3.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-s[-1]]


def encrypt(plaintext, key):
    plaintext = pad(plaintext)
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode('utf-8')


def decrypt(ciphertext, key):
    text = base64.b64decode(ciphertext)
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)
    s = cipher.decrypt(text)
    s = unpad(s)
    return s.decode('utf-8')


key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print(f'Ключ: {key}')
while True:
    print('Выберите:\n\t1 - Зашифровать\n\t2 - Расшифровать\n\t'
          '3 - Выход из программы\n\t')
    operation = input('Ваш выбор: ')
    if operation == '1':
        plaintext = input("Введите строку: ")
        print(encrypt(plaintext, key))
    if operation == '2':
        ciphertext = input("Введите строку: ")
        print(decrypt(ciphertext, key))
    else:
        if operation == '3':
            print('Выход...')
            break
