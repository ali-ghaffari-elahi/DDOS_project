###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 48 Date: 20/12/2012 DtD: 1145 Copyright:(c)MrHs 2012'''
import socket

host=""
test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.connect((host,23573))
for i in range(10):
    a=test.recv(2**16)
    print(a.decode())
    test.send((input("Please answer :")).encode())
    
a=(test.recv(2**20)).decode()
print("your final result is :\n"+a)
#Comment :
