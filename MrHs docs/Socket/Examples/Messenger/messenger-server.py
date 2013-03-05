###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 43 Date: 19/12/2012 DtD: 1146 Copyright:(c)MrHs 2012'''
import socket

test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.bind(("",32000))
test.listen(1)
sender=socket.gethostname()
(client,addr)=test.accept()
client.send("Connection established".encode())

print("Passed")
while 1:
    print(client.recv(2**16))
    a=sender+" :"+input(">>>")    
    client.send(a.encode())
    






#Comment :
