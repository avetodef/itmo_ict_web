import socket
def connect(sock):
    HOST = "localhost"
    PORT = 8888
    sock.connect((HOST, PORT))

def send_msg(sock, msg):
    sock.send(str(msg).encode())

if __name__ == "__main__":
    
    print("connecting to server.....")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(sock)

    print("connected to server")

    #   Клиент запрашивает у сервера выполнение математической операции, 
    #   параметры, которые вводятся с клавиатуры.

    h = float(input("enter height "))
    send_msg(sock, h)

    a = float(input("enter side "))
    send_msg(sock, a)

    s = sock.recv(1024)
    print("surface is ", s)
    
    sock.close()
