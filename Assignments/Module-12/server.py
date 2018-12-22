import socket
import select
import threading
import csv

file_name = "data.csv"

# fields = []
rows = []

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # fields = csv_reader.next()

    for row in csv_reader:
        rows.append(row)
final_list = []
for row in rows:
    for i in range(0, 3):
        final_list.append(row[i])



def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(10)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        threading.Thread(target = FindMe, args = (c, addr)).start()

def FindMe(c, addr):
    index = 0
    connection = True
    while connection:
        option1 = 'Attendence-Success'
        option2 = 'Attendence-Failure'
        data = c.recv(1024).decode()
        # data = int(data)
        if not data:
            break
        print ("from connected user : " + str(data))
        for i in final_list:
            if i == data:
                index = final_list.index(i)
            else:
                out = "Roll Number not found"
                c.send(str(out).encode())
        question = final_list[index+1]
        answer = final_list[index+2]
        c.send(str(question).encode())
        user_answer = c.recv(1024).decode()
        if(answer == user_answer):
            c.send(str(option1).encode())
            connection = False
            break
        else:
            c.send(str(option2).encode())
    print("server closed from" + str(addr))
    c.close()

# num = random.randrange(1,51)

if __name__ == '__main__':
    Main()