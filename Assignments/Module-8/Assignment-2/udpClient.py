import socket

def Main():
	host = '127.0.0.2'
	port = 5001

	# Server that we are sending to 
	server = ('127.0.0.2', 6000)

	#Create a socket

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Enter <currency> value To <currency>")
	message = input()
	while message != 'q':
		s.sendto(str.encode(message), server)
		data, address = s.recvfrom(1024)
		print("output :"+str(data.decode()))
		message = input()
	s.close()

if __name__ == '__main__':
	Main()