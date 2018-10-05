import socket

sock = socket.socket()
sock.connect(('192.168.1.101', 8080))

while 1:
	cmd = input("$>")
	sock.send(cmd.encode())
	data = sock.recv(1024)
	print (data.decode())
	if not data:
		sock.close()

sock.close()
