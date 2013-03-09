###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 58 Date: 9/3/2013 DtD: 1065 Copyright:(c)MrHs 2013'''

import socket

#(***** Constants *****

host=socket.gethostbyname()
port=1373
#*********************)
address=socket.getaddrinfo(host,port)
mainSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mainSocket.bind(address)
mainSocket.listen(5)

#**************************
clientList=[]  #A list of address of all clients
stop=False


def reciever(mainSocket):
    global stop
    clientList=[]
    while not stop:
        mainSocket.listen(5)
        clientList.append(mainSocket.accept()) 
    return alientList
def stopper():
    global stop
    stop=True
    


"""Here should be a function that
unless the user stop it listens to the network to accept new clients
"""

#**************************





#Comment :
