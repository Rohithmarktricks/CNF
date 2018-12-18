# tcpServer.py
import socket

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	connection, address = s.accept()
	print("Connection from: " +str(address))
	while True:
		data = connection.recv(1024)
		if not data:
			break
		print("from connected user: "+str(data))
		data = str(data).upper()
		connection.send(str.encode(data))
	connection.close()

if __name__ == '__main__':
	Main()