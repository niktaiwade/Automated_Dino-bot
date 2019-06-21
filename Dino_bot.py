import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *
import time

class cordinates():
    replay = (343, 231)
    dino = (173,241)
    #xcord=
  #323,232,344,248

def restart():
    pyautogui.click(cordinates.replay)

def space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def image():
    box = (221,243,265,273)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a.sum())
    return a.sum()

def main():
    restart()
    while True:
        if(image()!=1575):
            space()
            time.sleep(0.1)

main()