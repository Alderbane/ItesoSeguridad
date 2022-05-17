import socket, sys


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

file = open('./message.txt', 'rb')
data = file.read() 

eFile = open('./encrypted.txt', 'wb')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)
    data = s.recv(1024)
    eFile.write(data)
    
