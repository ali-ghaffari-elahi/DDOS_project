import threading

bol = False

def hooman():
    global bol
    while bol:
        for i in range(5):
            print "shalgham" + "\t" + str(i) 
        bol = not bol    

def booll():
    global bol
    while not bol:
        print "bool value has been changed"
        bol = not bol

string = "salam this is multithreading"
thread = []
thread.append(threading.Thread(target = hooman))
thread.append(threading.Thread(target = booll))
for i in range(2):
    thread[i].daemon = True
    thread[i].start()
"""
for i in range(5):
    thread.append(threading.Thread(target=hooman(string,i)))
    thread[i].daemon = True
    thread[i].start()
"""


