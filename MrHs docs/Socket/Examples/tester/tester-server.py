###########################################################################
# MM          MM            HH      HH                  CCCCCCC  EEEEEEEE #
# MMMMM     MMMM  rr  rr    HH      HH     ssss        C         E        #
# MM  MM  MM  MM  rrrr  rr  HHHHHHHHHH  ss            C          EEEEEEEE #
# MM    MM    MM  rrr       HHHHHHHHHH    s           C          EEEEEEEE #
# MM          MM  rr        HH      HH     s  ss       C         E        #
# MM          MM  rr        HH      HH  sssss           CCCCCCC  EEEEEEEE #
###########################################################################
##                        Written in python 3.3
'''Program number: 47 Date: 20/12/2012 DtD: 1145 Copyright:(c)MrHs 2012'''
import socket

ask=open("questions.csv","r")
result=open("result.txt","w")
qlist=ask.readlines()
host=socket.gethostname()
test=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
test.bind((host,23573))
test.listen(2)
(client,addr)=test.accept()
for i in qlist:
    print(i)
    answer=i.partition("__")[2].partition("\n")[0]
    answer=answer.split()
    for j in range(len(answer)):
        if answer[j][0]=="*":
            correct=j+1
            answer[j]=answer[j][1:]
    ans=""        
    for m in range(1,5):
        ans+=str(m)+")"+answer[m-1]+"  "
    client.send((i.partition("__")[0]).encode())
    client.send(ans.encode())
    cans=client.recv(4)
    cans=int(cans.decode())
    if cans==correct:
        result.writelines("correct\n")
    if cans!=correct:
        result.writelines("wrong\n")
result.close()
result=open("result.txt","r")
ans=str(result.read()).encode()
client.send(ans)
client.close()


#Comment :
