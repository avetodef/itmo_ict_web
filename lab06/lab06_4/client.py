import socket
import threading

HOST = 'localhost'
PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def send():
    while True:
        message = input('')
        client_socket.send(message.encode('utf-8'))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("error occured")
            client_socket.close()
            break


send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)

send_thread.start()
receive_thread.start()
