# FUCK FIDDLE

import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time

pyautogui.FAILSAFE = False
TIMELAPSE = 1

fidImg = './fid1.png'
goodbyeImg = './exit.png'
yesImg = './realexit.png'
myfidImg = './myfid.png'

def checkforenemyfiddle():

    while True:
        fid = imagesearch(myfidImg, 0.8)
        if not fid[0] == -1:
            print("ENEMY FIDDLESTIX FOUND, EXITING IMMEDIATELY")
            break
        time.sleep(TIMELAPSE)
    print('out of loop')
    quitgame()
    exit()


def quitgame():
    goodbye = imagesearch(goodbyeImg, 0.8)
    
    
    if not goodbye[0] == -1:
        pyautogui.click(goodbye[0], goodbye[1])
    else:
        print('cant find x button')
    
    yes = imagesearch(yesImg, 0.8)
    if not yes[0] == -1:
        pyautogui.click(yes[0], yes[1])
    else:
        print('cant find exit button')


def main():
    checkforenemyfiddle()



if __name__ == '__main__':
    print("Looking for fiddle...")
    main()