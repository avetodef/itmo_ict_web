# 3.	Реализовать серверную часть приложения. Клиент подключается к серверу. 
#   В ответ клиент получает http-сообщение, содержащее html-страницу, 
#                                          которую сервер подгружает из файла index.html.

import socket

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

    try:
        file = open("lab.html", "r")
        data = file.read()
        
        response = """HTTP/1.0 200 OK
Content-Type: text/html \n \n
        """
        response += data

        print(response)

        conn.send(response.encode("UTF-8"))
    except FileNotFoundError:
        print("file not found :(")
    print("end")
    

