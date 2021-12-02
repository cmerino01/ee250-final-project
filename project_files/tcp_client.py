"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""

# Github repo link: https://github.com/usc-ee250-fall2021/lab03-lab3-imtiaz/tree/lab03/ee250/lab03
# Team Member Name: Imtiaz Uddin

import socket
from crypto_machine import main_dict

def server_fun():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("40.118.164.114", 8080))
    # For testing on local machine: "127.0.0.1", 10002
    
    # TODO: Get user input and send it to the server using your TCP socket
    text = input("Enter user input: ").encode()
    s.send(text)
    
    # TODO: Receive a response from the server and close the TCP connection
    print(s.recv(1024).decode())
    s.close()