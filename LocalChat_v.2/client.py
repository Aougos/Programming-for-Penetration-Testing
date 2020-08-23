import socket

ip = socket.gethostname() #ip client
port = 1111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))

message = input ("--> ")

while message.lower().strip() != "bye": 
    s.send(message.encode())

    feedback = s.recv(1024).decode()
    print("feedback: " + str(feedback))

    # print("--> " + feedback)
    message = input ("--> ")
    
s.close()