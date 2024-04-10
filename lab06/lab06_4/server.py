import socket
import threading

HOST = 'localhost'
PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []
def broadcast(message, cur):
    for client in clients:
        if (client != cur):
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print('got message ', message, " from ", client)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break
def receive():
    while True:
        client, addr = server_socket.accept()
        print ("connected to ", addr)
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server up")
receive()
