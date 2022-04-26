import socket, nacl.utils, sys, nacl.secret
from AES256 import AESCipher
from Aleatorios import genRandStr
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
aes = AESCipher(key)

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


randStr = genRandStr(256).strip()

encrypted = aes.encrypt(randStr)
print(randStr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encrypted)
    data = s.recv(1024)
    data = aes.decrypt(data)
print(f"{data!r}")