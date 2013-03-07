###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 44 Date: 19/12/2012 DtD: 1146 Copyright:(c)MrHs 2012'''
import socket
from threading import *
test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.connect(("127.0.0.1",31001))
sender=socket.gethostname()
print(test.recv(2**8))

def send(s):
    massage = str(raw_input(">>> "))
    if massage:
        s.send(massage.encode())

def recv1(s,sender):
    data = s.recv(2**8)
    if data:
        print sender,data

t= [Thread(target = recv1(test,sender)),Thread(target = send(test))]
#while 1:
for i in range(2):
    t[i].start()
"""
while 1:    
    test.send(sender+" :"+input(">>>"))
    print(test.recv(2**16))

"""
