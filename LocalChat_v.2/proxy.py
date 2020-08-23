import socket
#client side
ip = socket.gethostname()
port = 1111
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(3)
con, addr = s.accept()

#server side
ip_server = socket.gethostname()
port_server = 2222
socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_to_server.connect((ip_server,port_server))

str_filter = ["script", "sys", "root", "alert", "manusia"]
while True: 
    msg = con.recv(1024).decode()
    if msg in str_filter: 
        # dibanned
        con.send("Failed send message".encode())
    else:   
        #berhasil
        socket_to_server.send(msg.encode())
    msg_server = socket_to_server.recv(1024).decode()
    while msg_server != None:
        con.send(msg_server.encode())
        break

socket_to_server.close()
s.close()

# ref:
# Kelas zi
# Materi Kelas
# Client & Server dari assignment pertama