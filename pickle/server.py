import socket
from person import Person
import pickle

IP = "127.0.0.1"  # IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# bind socket to ip address and port
server.bind(('127.0.0.1',9999))


person1 = Person("John", "50")


def start_server(isConnected):
    server.listen()
    print("Server is running")
    while isConnected:
        client, addr = server.accept()
        msg = pickle.dumps(person1)
        client.send(msg)
        isConnected = False

if __name__=='__main__':
    connected = True
    start_server(connected)