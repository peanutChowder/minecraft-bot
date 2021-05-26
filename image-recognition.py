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
        # temp. delete below.
        keyboard.wait("k")

        with mss.mss() as sct:
            while self.continueSearch:
                screenshot = np.array(sct.grab(self.monitor))
                mask = self.colorFilter(screenshot)
                x, y = self.getBestMatchLoc(mask)

                if x and y:
                    pass

    def mineOre(x, y):
        pyautogui.moveTo(x, y, 0.3)
        pyautogui.click(duration=2)

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