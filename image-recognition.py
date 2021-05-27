import numpy as np
import cv2 as cv
from time import sleep
import mss 
import pyautogui

#TODO delete
import keyboard

class OreRecognition():
    def __init__(self):
        self.continueSearch = True
        self.screenshotInterval = 1
        self.monitor = {"top": 32, "left": 0, "width": 960, "height": 550}

        self.lower_blue = np.array((56, 150, 145))
        self.upper_blue = np.array((181, 245, 242))

    def oreSearch(self):
        tempIter = 1
        with mss.mss() as sct:
            # while self.continueSearch:
            while tempIter > 0:
                screenshot = np.array(sct.grab(self.monitor))
                mask = self.colorFilter(screenshot)
                x, y = OreRecognition.getBestMatchLoc(mask)

                if x and y:
                    OreRecognition.mineBlock(x, y)

                # TODO: delete
                tempIter -= 1

    def mineBlock(x, y):
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        sleep(1)
        pyautogui.mouseUp()
        # pyautogui.moveRel(350, 0, 0.5)

    def colorFilter(self, screenshot):
        hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)
        mask = cv.inRange(hsv, self.lower_blue, self.upper_blue)
        return mask

    def getBestMatchLoc(mask):
        _, maxValue, _, maxLocation = cv.minMaxLoc(mask)
        if maxValue:    # Check if the max value is nonzero
            return maxLocation
        else:
            return (0, 0)


# TODO: delete
print("waiting on input")
keyboard.wait("k")
oreBoy = OreRecognition()
oreBoy.oreSearch()
