import socket
import random
import threading


port_list = []
def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(10)

    while True:
        c, addr = s.accept()
        # print(c)
        print ('connection from : '+ str(addr))
        # print(addr[1])
        port_list.append(addr[1])
        initial = 'welcome to guess my number'
        c.send(str(initial).encode())
        threading.Thread(target = Guess, args = (c, addr)).start()

def Guess(c, addr):
    count = 0
    connection = True
    num = random.randrange(1,51)
    while connection:
        option1 = "correct! Number of guesses is "+str(count)
        option2 = 'your number is less than guess'
        option3 = 'your number is greater than guess'
        data = c.recv(1024).decode()
        count += 1
        data = int(data)
        if not data:
            break
        print ("from connected user :{} {} ".format(str(data), addr[1]))
        if(data == num):
            # c.send(str(item1).encode())
            c.send(str(option1).encode())
            connection = False
            break
        elif(data < num):
            # c.send(str(item2).encode())
            c.send(str(option2).encode())
        elif(data >  num):
            # c.send(str(item3).encode())
            c.send(str(option3).encode())
    print("server closed from" + str(addr))
    c.close()

if __name__ == '__main__':
    Main()