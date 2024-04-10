# 1. Реализовать клиентскую и серверную часть приложения. 
# Клиент отсылает серверу сообщение «Hello, server».
# Сообщение должно отразиться на стороне сервера. 
# Сервер в ответ отсылает клиенту сообщение «Hello, client». 
# Сообщение должно отобразиться у клиента.


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
PORT = 8888

sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print('connected to client ', addr)

msg = "HELLO, CLIENT"


data = conn.recv(1024)
print(data)
conn.send(msg.encode())

conn.close()
