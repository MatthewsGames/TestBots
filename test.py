import pyautogui
pyautogui.FAILSAFE = True
while True:
    for i in pyautogui.locateAllOnScreen('black.png'):
        if(i[1] > 500):
            pyautogui.click(x=i[0]+20,y=i[1]+20)
            print(i[0],i[1])
            break