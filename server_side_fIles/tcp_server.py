import socket
import pickle
import sys

from plot_data import plot

#set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#allow any IP to be commincated with via port 8080 (easier to do all 0's)
s.bind(("0.0.0.0", 8080))
#listen for any tx
s.listen()
#accept tx
conn, addr = s.accept()
try:
    with conn:
        #connection establish message
        print('Connected by', addr)
        while True:
            #take in data
            data = conn.recv(1024)
            if not data:
                continue
                print("test")
            else:
                #unpack pickle
                crypto_data = pickle.loads(data)
                print(crypto_data)
                #crypto_data  = json.loads(crypto_data)
                #link = plot(crypto_data)
                conn.sendall(("checkpoint").encode()) #final sendall message should be link
except KeyboardInterrupt:
    s.close()
