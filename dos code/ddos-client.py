###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 59 Date: 9/3/2013 DtD: 1065 Copyright:(c)MrHs 2013'''

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#*****Constants
host=""
port=1373
address=socket.getaddrinfo(host,port)
#*****/Constants


client.connect(address)



if client.recv(2**10):
    pass
    #Here should be the pinging application




#Comment :
