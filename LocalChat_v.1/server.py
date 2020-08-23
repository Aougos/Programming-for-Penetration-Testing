import socket  
def server_program():     
	host = socket.gethostname() # ambil IP kita     
	port = 5000  # set port yg kita inginkan.     
	# dalam yang saya baca di web, tidak disarankan menge-set port dibawah 1024, karena sudah “dipesan” oleh pc kita secara default untuk hal lain     
	# print(f"{host}") #test ip  
    
    server_socket = socket.socket()  # get instance     
    server_socket.bind((host, port))  # bind host address and port together. Bind menjadikan server menjadi ‘tuple’  
    
    # set ‘jumlah client’ yang bisa terhubung ke server     
    server_socket.listen(2)     
    conn, address = server_socket.accept()  # buka koneksi     
    print("Connection from: " + str(address))   

    while True:         
    	# receive data stream. it won't accept data packet greater than 1024 byte s         
    	data = conn.recv(1024).decode()         
    	#conn.recv('1024') membaca '1024' bytes         
    	if not data:             
    		break         
    	print("from connected user: " + str(data))                  
    	# version 1 = admin adalah manusia         
    	# data = input(" -> ")         
    	# conn.send(data.encode())  
        
        # version 2 = admin adalah system (simple chatbot)         
        a = (" -> ")         
        print (a)         
        if(data == "hai"):             
        	conn.send(("hai").encode())         
        if(data == "hmm"):             
        	conn.send(("apa").encode())                 
        if(data == "bye"):             
        	conn.close()         
        else:             
        	conn.send(("silahkan menghubungi 012 667 889").encode())  
    conn.close()  # close the connection 

if __name__ == '__main__':     
	server_program()  

# # ref: # https://stackoverflow.com/questions/7174927/when-does-socket-recvrecv-sizereturn 
# https://stackoverflow.com/questions/21233340/sending-string-via-socket-python 
# materi kelas