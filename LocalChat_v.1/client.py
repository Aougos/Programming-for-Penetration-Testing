import socket #menggunakan module untuk terhubung ke system  

# host = socket.gethostname() #dapetin namaPC 
# hostIP = socket.gethostbyname(host) #dapetin IP_PC 
# print(f"the host is {hostIP}")  

# server_socket.listen() #buka port  

def client_program(): #fungsi client_program     
	host = socket.gethostname()  # karena ini di 1 pc, jdi kita samain ip client dan server     
	port = 5000  # menggunakan port server  
    
    client_socket = socket.socket()  # instantiate     
    client_socket.connect((host, port))  # connect server  
    
    message = input(" -> ")  # input ‘chat’   
    
    while message.lower().strip() != 'bye':         client_socket.send(message.encode())  # kirim pesan          
	    data = client_socket.recv(1024).decode()  # terima response  
    
        print('Received from server: ' + data)  # print pesan  
    
        message = input(" -> ")  # kirim pesan  
    
    client_socket.close()  # putusin koneksi  

if __name__ == '__main__':     
	client_program()  

# ref: 
# https://pythontic.com/modules/socket/gethostname 
# https://www.journaldev.com/15906/python-socket-programming-server-client 