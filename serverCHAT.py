import socket
from threading import Thread

IP = '127.0.0.1'
PORT = 9999
clients = []
#create socket             AF_INET = IPv4 , SOCK_STREAM = TCP 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# keep port always available
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind socket to IP address and port
server.bind((IP, PORT)) #TUPLE

server.listen() #start listening for connections on defined port

def broadcast(msg):
    for client in clients:
        client.send(msg)
        
def handle_connection(client):
    stopped = False
    while not stopped:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            print("Wopsie")
            stopped = True

def start_server():
    print("Server is running")
    while True:
        #accent all connections
        client, port = server.accept()
        print(f"Connected from {client} on port {port}")
        client.send("USERNAME".encode())
        username = client.recv(1024).decode() 
        clients.append(client)
        
        broadcast(f"{username} has joined the chat".encode())
        
        thread = Thread(target = handle_connection, args=(client,))
        thread.start()

if __name__ == '__main__':  #start server function only if this file is being run
    start_server()