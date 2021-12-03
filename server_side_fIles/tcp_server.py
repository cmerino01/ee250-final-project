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
with conn:
    #connection establish message
    print('Connected by', addr)
    while True:
        #take in data
        data = conn.recv(1024)

        full_data += data
        crypto_data = pickle.loads(full_data[HEADERSIZE:])
        print(crypto_data)
        #testing - lines 18,22, and 23 are where I am getting issues. Maybe there is another way to tx dict?
        print("Received size:" + str(sys.getsizeof(data)))
        #unpack pickle
        #crypto_data = pickle.loads(data)
        #crypto_data  = json.loads(crypto_data)
        #link = plot(crypto_data)
        if not data:
            continue
        conn.sendall(("checkpoint").encode()) #final sendall message should be link
