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
from threading import *
test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.bind(("127.0.0.1",31001))
test.listen(1)
sender=socket.gethostname()
(client,addr)=test.accept()
client.send("Connection established".encode())

print("Passed")

bool = False
client_list = []

def while1(client,sender,test):
    global bool
    global client_list
    while bool:
        test.listen(5)
        client_list.append(test.accept())


def attack(client_list):
    massage = str(raw_input("attack--->>> "))
    client.send(massage.encode())



"""""
def send1(client):
    massage = str(raw_input(">>> "))
    client.send(massage.encode())

def recv(client,sender):
    data = client.recv(2**8)
    if data:
        print sender,data
        
t= [Thread(target = send1(test)), Thread(target = recv(test,sender))]

for i in range(2):
    t[i].start()

"""""
"""
while 1:
    print(client.recv(2**16))
    a=sender+" :"+input(">>>")    
    client.send(a.encode())
"""


