import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    # count = 0
    # initial = s.recv(1024)
    # print('received from server : '+ initial.decode())
    message = input("Mark Attendence Roll_no : ")
    while message != 'q':
        # count += 1
        s.send(message.encode())
        data = s.recv(1024)
        if(data.decode() == "Roll Number not found"):
            print("Roll Number not found")
            break
        else:
            print('Secret Question : ' + data.decode())
            answer = input("Secret Answer : ")
            s.send(answer.encode())
            ser_report = s.recv(1024).decode()
            if(ser_report == 'Attendence-Success'):
                print('Attendence-Success')
                break
    s.close()

if __name__ == "__main__":
    main()