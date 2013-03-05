import socket

host = "127.0.0.1"
port = 5080
size = 900 #size of resive pockets
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((host, port)) #connect the s to the host and port
s.listen(5) #listen to the port and host

print "wathing for other user"
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data == "con":
        break

print "now connected"
while 1:
    massage = str(raw_input("your massage"))
    client.send(massage)
    data = client.recv(size)
    if data:
        print "client(s) : ",data
