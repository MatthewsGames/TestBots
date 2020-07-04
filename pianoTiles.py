import pyautogui
from time import sleep
game = input("Game?: ")
pyautogui.FAILSAFE = True
method = 1
l = None
while l == None:
    l = pyautogui.locateOnScreen('chrome4.png')
pyautogui.click(x=l[0],y=l[1])
l = None
while l == None:
    l = pyautogui.locateOnScreen('expand.png')
pyautogui.click(x=l[0],y=l[1])
l = None
while l == None:
    l = pyautogui.locateOnScreen('star.png')
pyautogui.click(x=l[0],y=l[1])
pyautogui.typewrite("http://tanksw.com/piano-tiles/\n")
l = None
if(game.lower() == "relay"):
    while l == None:
        l = pyautogui.locateOnScreen('y.png')
if(game.lower() == "classic"):
    while l == None:
        l = pyautogui.locateOnScreen('Classic.png')
if(game.lower() == "rush"):
    while l == None:
        l = pyautogui.locateOnScreen('Rush.png')
if(game.lower() == "zed"):
    while l == None:
        l = pyautogui.locateOnScreen('Zed.png')
if(game.lower() == "arcade"):
    while l == None:
        l = pyautogui.locateOnScreen('Arcade.png')
pyautogui.click(x=l[0],y=l[1])
sleep(1)
c1 = 30,0
c2 = 130,0
c3 = 230,0
c4 = 330,0
while True:
    if(method == 2):
        img = pyautogui.screenshot(region=(520,550,400,1))
        if(img.getpixel(c1) == (17,17,17,255)):
            pyautogui.click(x=550,y=550)
        elif(img.getpixel(c2) == (17,17,17,255)):
            pyautogui.click(x=650,y=550)
        elif(img.getpixel(c3) == (17,17,17,255)):
            pyautogui.click(x=750,y=550)
        elif(img.getpixel(c4) == (17,17,17,255)):
            pyautogui.click(x=850,y=550)
    else:
        l = pyautogui.locateOnScreen('tile3.png',region=(520,550,400,1))
        if(l != None):
            pyautogui.click(x=l[0], y=l[1])