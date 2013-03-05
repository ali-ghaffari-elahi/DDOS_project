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

test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.connect(("169.254.211.104",32010))
sender=socket.gethostname()
print(test.recv(2**16))
while 1:    
    test.send(sender+" :"+input(">>>"))
    print(test.recv(2**16))


#Comment :
