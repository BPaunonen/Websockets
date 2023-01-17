import socket
import pickle

IP = "127.0.0.1"  # IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

connected = True

while connected:
    msg = client.recv(1024)
    person = pickle.loads(msg)
    print(person.name)
    connected = False
    



client.close()