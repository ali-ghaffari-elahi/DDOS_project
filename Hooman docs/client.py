import socket

host = "127.0.0.1"
port = 5080
size = 900 #size of resive pockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port)) #coonect to the host and port

s.send("con") #for activating the server to know that a client connected

while 1:
    massage = str(raw_input("you : "))
    data = s.recv(size)
    if data:
        print "server : ",data
    if massage:
        s.send(massage)

