import pyautogui
from time import sleep
import random
pyautogui.FAILSAFE = True
prevx = 0
prevy = 0
r = 0
x = 0
y = 0
# w=550 h=150 x=450 y=650
t = 0
while True:
    if(t >= 5):
        pyautogui.click(x=250, y=500)
        sleep(6)
        pyautogui.click(x=725, y=420)
        t = 0
    x = random.randint(450,950)
    y = random.randint(650,775)
    r = (x,y,50,50)
    prevx = x
    prevy = y
    l = pyautogui.locateOnScreen('brown.png',region=r)
    if(l == None):
        l = pyautogui.locateOnScreen('brown2.png', region=r)
    if(l != None):
        pyautogui.click(x=l[0], y=l[1])
        sleep(3)
        pyautogui.click(x=460, y=835)
        sleep(0.5)
        pyautogui.click(x=460, y=580)
        sleep(10 + random.randint(0,10)/10)
        t += 1

