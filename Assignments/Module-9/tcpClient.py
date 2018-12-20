import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    initial = s.recv(1024)
    print('received from server : '+ initial.decode())
    message = input("Enter your guess : ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print('received from server : ' + data.decode())
        if(data.decode() == 'correct!'):
            break
        message = input("Enter your guess : ")
    s.close()

if __name__ == "__main__":
    main()