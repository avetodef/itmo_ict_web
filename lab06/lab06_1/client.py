import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
PORT = 8888
sock.connect((HOST, PORT))

msg = "HELLO, SERVER"

sock.send(msg.encode())

data = sock.recv(1024)
print(data)
sock.close()