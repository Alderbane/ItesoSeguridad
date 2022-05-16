from AES256 import AESCipher
from nacl.signing import SigningKey
import socket,nacl.secret,nacl.utils

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
aes = AESCipher(key)



HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


privFile = open('./priv.key', 'wb')
pubFile = open('./pub.key', 'wb')
logsFile = open('./logs.txt', 'a')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode('utf-8')
            encrypted = aes.encrypt(data)
            
            signing_key = SigningKey.generate()
            signed = signing_key.sign(encrypted)
            privFile.write(signing_key._signing_key)
            pubFile.write(signing_key.verify_key._key)

            logsFile.write("Uploaded file by client\n")

            conn.sendall(signed)
            if not data:
                break
            