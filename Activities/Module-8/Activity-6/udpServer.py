import socket

def Main():
	host = '127.0.0.1'
	port = 5003

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Server started......")
	while True:
		data, address = s.recvfrom(1024)
		print("Message recived from :"+str(address))
		print("From connected address: "+str(data))
		data = str(data).upper()
		print("Sending: "+str(data))
		s.sendto(str.encode(data), address)
	s.close()

if __name__ == '__main__':
	Main()
