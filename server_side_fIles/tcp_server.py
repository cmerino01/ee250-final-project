import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("168.62.194.224", 8080))
s.listen()
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)