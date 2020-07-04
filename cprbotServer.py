import socket
from _thread import *
import sys
import threading
names = ["Bob13243242","Bob1213213","Bob3224564","Bob2236344","Bob2545354","Bob6546546","Bob35453534","Bob65465443","Bob9869545","Bob88883243","Bob9938324"]
server = "10.0.1.48"
nameNumber = 0
port = 5560
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
global info
info = "Start"
try:
    s.bind((server,port))
except socket.error as e:
    str(e)
s.listen()
print("Waiting for connection, Server Started")
def takeInput():
    inp = ""
    print("Beginning input")
    while inp != "terminate -a":
        inp = input()
        global info
        info = inp
def threaded_client():
    conn.send(str.encode("Connected"))
    print("Added player")
    while True:
        try:
            data = conn.recv(4096).decode()
            if not data:
                print("Disconnected")
                break
            if(data == "name?"):
                global nameNumber
                conn.sendall(str.encode(names[nameNumber]))
                nameNumber += 1
            global info
            conn.sendall(str.encode(info))
        except:
            break
    print("Lost connection")
    conn.close()
threading.Thread(target=takeInput).start()
while info != "terminate -a":
    conn, addr = s.accept()
    print("Connected to:",addr,info)
    threading.Thread(target=threaded_client).start()
print(info)