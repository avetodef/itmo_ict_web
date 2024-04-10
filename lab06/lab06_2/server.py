# 2 Реализовать клиентскую и серверную часть приложения. 
#   Клиент запрашивает у сервера выполнение математической операции, 
#   параметры, которые вводятся с клавиатуры.
#   Сервер обрабатывает полученные данные и возвращает результат клиенту. Вариант:

# d.	Поиск площади параллелограмма.

import socket

def surface_of_parallelogram(a, h):
    return float(a)*float(h);

def send_msg(conn, msg):
    conn.send(msg.encode())

def connect(sock):
    HOST = "localhost"
    PORT = 8888
    sock.bind((HOST, PORT))

if __name__ == "__main__":
    print("waiting for client...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(sock)
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected to client ', addr)

    h = conn.recv(1024)
    a = conn.recv(1024)
    s = surface_of_parallelogram(a, h)

    send_msg(conn, str(s))

    conn.close()