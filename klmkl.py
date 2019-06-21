import time
from numpy import *
from PIL import ImageOps, ImageGrab
import pyautogui

class Cordinates():
    replayBtn= (377, 407)
    dinosaur = (369, 418)

def restart():
    pyautogui.click(Cordinates.replayBtn)

def space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('jump')
    pyautogui.keyUp('space')

restart(
time.sleep(1)