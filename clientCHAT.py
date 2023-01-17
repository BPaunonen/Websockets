
from login import Ui_Form as login_form
from ui_chat import Ui_Form as chat_form
from PySide6 import QtWidgets as qtw
import socket
from threading import Thread
import datetime

import json

IP = "127.0.0.1"  # IP = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class LoginWidget(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = login_form()
        self.ui.setupUi(self)
        self.ui.button_LOGIN.clicked.connect(self.login)
        
        
    def login(self):
        self.username = self.ui.txt_USERNAME.toPlainText()
        print(self.username)
        self.hide()
        self.widget = ChatWidget(self.username)
        self.widget.show()
        self.connect()
        
    def connect(self):
        client.connect((IP, PORT))
        msg = client.recv(1024).decode('utf-8')
        if msg == "USERNAME":
            client.send(self.username.encode())
            thread = Thread(target = self.widget.receive)
            thread.start()

class ChatWidget(qtw.QWidget):
    def __init__(self, username):
        super().__init__()
        self.ui = chat_form()
        self.ui.setupUi(self)
        self.username = username
        self.ui.button_SEND.clicked.connect(self.send_message)
        
        #fetch previous messages from JSON file
        self.get_message()
    
    def get_message(self):
        try:
            with open('messages.json', 'r') as file:
                contents = json.load(file)
                for i in range(len(contents)):
                    time = contents[i]['time']
                    sender = contents[i]['name']
                    message = contents[i]['message']
                    msg = f"{time}---{sender}: {message}"
                    self.ui.listWidget.addItem(msg)
        
        except FileNotFoundError as e:
            print("File not found")
            print(e)
    
    def receive(self):
        stopped = False
        while not stopped:
            msg = client.recv(1024).decode()
            self.ui.listWidget.addItem(msg)
            
    def send_message(self):
        now = datetime.datetime.now() # hakee sen hetkisen ajan
        current_time = now.strftime("%H:%M:%S")
        now_time = datetime.datetime.now()
        message = self.ui.textEdit.toPlainText()
        message_to_send = (now_time.strftime('%Y-%m-%d %H:%M:%S')) + " " + self.username + ": " + message
        client.send(message_to_send.encode())
        self.ui.textEdit.clear() # cler the text field after sending message

        message = {'time':current_time, 'name':self.username , 'message':message}
        try:
            with open('messages.json') as file:
                file_data = []
                file_data = json.load(file)
                file_data.append(message)
            with open('messages.json','w') as file:
                json.dump(file_data, file, indent = 4)
        except FileNotFoundError as fe:
            print('File not found')
            print(fe)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = LoginWidget()
    widget.show()
    app.exec_()
