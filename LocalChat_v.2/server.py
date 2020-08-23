import socket

ip = socket.gethostname()
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(2)
con, addr = s.accept()

while True: 
    msg = con.recv(1024).decode("utf-8")
    if not msg:
        break
    else:
        print("--> " + str(msg))
        msg = input("--> ")
        con.send(msg.encode())

s.close()