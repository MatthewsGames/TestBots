import pyautogui
import random
y = 0
numBots = 4
game = "Shooty"
pyautogui.FAILSAFE = True
l = None
while l == None:
    l = pyautogui.locateOnScreen('chrome3.png')
pyautogui.click(x=l[0],y=l[1])
l = None
while l == None:
    l = pyautogui.locateOnScreen('expand.png')
pyautogui.click(x=l[0],y=l[1])
for i in range(numBots):
    l = None
    while l == None:
        l = pyautogui.locateOnScreen('star.png')
    pyautogui.click(x=l[0],y=l[1])
    pyautogui.typewrite("matthewsgames.github.io\n")
    if(game == "Stabby"):
        for z in range(100):
            pyautogui.keyDown("down")
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('s8.png')
            if(l == None):
                l = pyautogui.locateOnScreen('s5.png')
        pyautogui.click(x=l[0] + 20,y=l[1] + 5)
    elif(game == "Shooty"):
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('s2.png')
        pyautogui.click(x=l[0] + 20, y=l[1] + 5)
    l = None
    while l == None:
        l = pyautogui.locateOnScreen('plus2.png')
    y = l[1]
    pyautogui.typewrite("NotBot" + str(i+1) + "\n")
    if(i != numBots - 1):
        pyautogui.click(x=l[0], y=l[1])
out = []
for i in range(numBots):
    out.append(False)
while True:
    for i in range(numBots):
        if(not out[i]):
            pyautogui.click(x=20 + i*240,y=20)
            rand1 = random.randint(60, 1380)
            rand2 = random.randint(75, 675)
            pyautogui.click(x=rand1, y=rand2)
            rand = random.randint(1,4)
            rand1 = random.randint(60,1380)
            rand2 = random.randint(75,675)
            if(rand == 1):
                pyautogui.keyDown("a")
                pyautogui.keyDown("left")
                if (pyautogui.locateOnScreen("win.png", region=(60, 150, 150, 150))):
                    for i in range(numBots):
                        out[i] = False
                pyautogui.keyUp("a")
                pyautogui.keyUp("left")
            elif(rand == 2):
                pyautogui.keyDown("w")
                pyautogui.keyDown("up")
                if (pyautogui.locateOnScreen("win.png", region=(60, 150, 150, 150))):
                    for i in range(numBots):
                        out[i] = False
                pyautogui.keyUp("w")
                pyautogui.keyUp("up")
            elif (rand == 3):
                pyautogui.keyDown("s")
                pyautogui.keyDown("down")
                if (pyautogui.locateOnScreen("win.png", region=(60, 150, 150, 150))):
                    for i in range(numBots):
                        out[i] = False
                pyautogui.keyUp("s")
                pyautogui.keyUp("down")
            elif (rand == 4):
                pyautogui.keyDown("d")
                pyautogui.keyDown("right")
                if(pyautogui.locateOnScreen("win.png",region=(60,150,150,150))):
                    for a in range(numBots):
                        out[a] = False
                pyautogui.keyUp("d")
                pyautogui.keyUp("right")
            if(game == "Shooty"):
                if(pyautogui.locateOnScreen("out.png",region=(300,425,800,100)) != None and not out[i]):
                    out[i] = True
                    print("Player",i,"is out.")
                    allOut = True
                    for a in out:
                        if(not a):
                            allOut = False
                    if(allOut):
                        for a in range(numBots):
                            out[a] = False
