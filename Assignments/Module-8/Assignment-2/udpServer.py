import socket
sample_dict = {"Dollar":[1, 67, 0.75, 113.41], "INR":[1/67, 1, 0.75/67, 113.41/67], "Pounds":[1/0.75, 67/0.75, 1, 113.41/0.75], "Yen":[1/113.41, 67/113.41, 0.75/113.41, 1]}


def Main():
	def Currency_converter(source, value, dest ):
		if source == "Dollar":
			if dest == "INR":
				return value*sample_dict.get("Dollar")[1]
			elif dest == "Pounds":
				return value*sample_dict.get("Dollar")[2]
			elif dest == "Yen":
				return value*sample_dict.get("Dollar")[3]

		if source == "INR":
			if dest == "Dollar":
				return value*sample_dict.get("INR")[0]
			elif dest == "Pounds":
				return value*sample_dict.get("INR")[2]
			elif dest == "Yen":
				return value*sample_dict.get("INR")[3]

		if source == "Pounds":
			if dest == "Dollar":
				return value*sample_dict.get("Pounds")[0]
			elif dest == "INR":
				return value*sample_dict.get("Pounds")[1]
			elif dest == "Yen":
				return value*sample_dict.get("Pounds")[3]

		if source == "Yen":
			if dest == "Dollar":
				return value*sample_dict.get("Yen")[0]
			elif dest == "INR":
				return value*sample_dict.get("Yen")[1]
			elif dest == "Pounds":
				return value*sample_dict.get("Yen")[2]

	host = '127.0.0.2'
	port = 6000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Server started......")
	while True:
		data, address = s.recvfrom(1024)
		print("Message recived from :"+str(address))
		print("From connected address: "+str(data))
		data = str(data.decode())
		message = data.split(" ")
		value = int(message[2])
		source = message[1]
		dest = message[4]
		new_data = Currency_converter(source, value, dest)
		print("Sending: "+str(new_data))
		s.sendto(str.encode(str(new_data)), address)
	s.close()

if __name__ == '__main__':
	Main()
