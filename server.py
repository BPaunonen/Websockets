import socket
import random

IP = "127.0.0.1"  # IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# bind socket to ip address and port
server.bind(('127.0.0.1',9999))

def start_server():
    server.listen()
    client, addr = server.accept()
    answer = random.randint(0,10)
    solved = False
    client.send("Arvaa luku väliltä 0-10".encode())
    while not solved:              
        guess = client.recv(1024).decode()
        if (int(guess) < answer):
            client.send("Liian pieni..".encode())
        elif (int(guess) > answer):
            client.send("Liian suuri!".encode())
        elif (int(guess)==answer):
            client.send("OIKEIN".encode())            
            solved = True

    print("Serveri suljetaan")
    server.close()

if __name__=='__main__':
    start_server()