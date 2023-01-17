import socket

IP = "127.0.0.1"  # IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

solved = False

while not solved:
    message_from_server = client.recv(1024).decode()
    if message_from_server =='OIKEIN':
        print("OIKEIN!!!")
        solved = True
    else:
        print(message_from_server)
        client.send(input("Arvaan luvun:").encode())        

client.close()