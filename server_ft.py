from socket import *
ss = socket(AF_INET,SOCK_STREAM)
ss.bind(("",1900))
ss.listen(5)
conn,addr = ss.accept()
print("Connection Established")
file = open("C:\\Users\\ASUS\\Documents\\cn fatlab\\output.txt","w")
data = conn.recv(1024)
file.write(data.decode())
print("File Successfuly coppied")
conn.close()
    
