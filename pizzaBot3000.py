import pyautogui
from time import sleep
pyautogui.FAILSAFE = True
speed = 100
while True:
    l = pyautogui.locateOnScreen("hotCheesePizza.png")
    if(l == None):
        l = pyautogui.locateOnScreen("cheesePizza.png")
        if(l == None):
            pass
        else:
            print("Cheese Pizza")
            l = None
            while l == None:
                l = pyautogui.locateOnScreen("crust.png",region=(230,750,975,1))
            pyautogui.mouseDown(x=325,y=500)
            pyautogui.moveTo(l[0] + 50,l[1] - 60,0)
            x = l[0]
            y = l[1]
            for i in range(5):
                pyautogui.move(0, -130,0.12)
                pyautogui.move(0, 130, 0.12)
            pyautogui.mouseUp()
            pyautogui.mouseDown(x=550, y=580)
            l = None
            while l == None:
                l = pyautogui.locateOnScreen("crust.png", region=(230, 750, 975, 10))
            pyautogui.moveTo(l[0] + 100,l[1])
            pyautogui.mouseUp()
            speed += 20

    else:
      print("Hot Cheese Pizza")
