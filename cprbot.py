import socket
import pyautogui
size = pyautogui.size()
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.1.11"
        self.port = 5561
        try:
            self.addr = (self.server, self.port)
            self.pos = self.connect()
        except:
            print("hi")

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
n = Network()
name = n.send("name?")
password = "TheC00leStPasSword"
response = ""
last = ""
while response != "terminate -a":
    response = n.send("ready")
    if(last != response):
        print(response)
        last = response
        if(response[0:4] == "goto"):
            print("Going to",response[4:])
        elif(response[0:5] == "start"):
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('chrome2.png')
            pyautogui.click(x=l[0], y=l[1])
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('expand.png')
            pyautogui.click(x=l[0], y=l[1])
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('star.png')
            pyautogui.click(x=l[0], y=l[1])
            pyautogui.typewrite("https://play.cprewritten.net/#/login\n")
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('3rd.png')
            pyautogui.click(x=size.width / 2, y=l[1])
            pyautogui.typewrite(name)
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('4th.png')
            pyautogui.click(x=size.width / 2, y=l[1])
            pyautogui.typewrite(password)
            l = None
            while l == None:
                l = pyautogui.locateOnScreen('5th.png')
            pyautogui.click(x=l[0], y=l[1])