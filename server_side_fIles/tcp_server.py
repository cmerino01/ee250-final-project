import socket
import pickle
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen()
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print("Received size:" + str(sys.getsizeof(data)))
        crypto_data = pickle.loads(data)
        #crypto_data  = json.loads(crypto_data)
        if not data:
            continue
        conn.sendall(("checkpoint").encode())
