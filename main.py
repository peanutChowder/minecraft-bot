import keyboard
import pyautogui
import time
import threading

class MinerBoy():     
    def __init__(self):
        self.currentlyWalking = False
        self.currentlyTunneling = False

        self.lookPxl = 280

        self.escapeKey = "k"

        self.continueMining = True
        self.cycleTime = 11

        self.torchPlacements = {"right": self.autoTorchRight, "down": self.autoTorchDown, "none": self.doNothing}

    def mineTunnel(self, cycles, placeTorch="right"):
        """
        Mines a straight tunnel. One cycle consists of mining for 'cycleTime' seconds.
        """
        # ensure camera is oriented correctly
        self.miningCamera()   

        while cycles > 0 and self.continueMining:
            self.toggleShiftWalk()
            self.toggleTunnel()
            time.sleep(self.cycleTime)
            self.toggleShiftWalk()
            self.toggleTunnel()
            self.torchPlacements[placeTorch]()
            cycles -= 1

    def clearArea(self, cycles, width):
        while width > 0 and self.continueMining:
            # TODO: make pythonic 
            self.mineTunnel(cycles, "down")
            self.mineDirectional(self.lookRight)
            self.mineDirectional(self.lookRight)

            self.mineTunnel(cycles, "none")
            self.mineDirectional(self.lookLeft)
            self.mineDirectional(self.lookLeft)

            width -= 1

    def mineDirectional(self, directionLook):
        """
        Mines a 2 block space in the adjacent direction and moves into the space
        """
        keyboard.press("shift")
        directionLook()
        self.miningCamera()

        pyautogui.mouseDown()
        time.sleep(1.5)
        pyautogui.mouseUp()

        # move
        keyboard.press("w")
        time.sleep(1)    # poor implementation due to possibility of no wall ahead
        keyboard.release("w")

        keyboard.release("shift")


    def toggleShiftWalk(self):
        if self.currentlyWalking:
            keyboard.release("shift")
            keyboard.release("w")
        else:
            keyboard.press("shift")
            keyboard.press("w")
        self.currentlyWalking = not self.currentlyWalking

    def toggleTunnel(self):
        if self.currentlyTunneling:
            pyautogui.mouseUp()
        else:
            pyautogui.mouseDown()
        self.currentlyTunneling = not self.currentlyTunneling

    def autoTorchRight(self):
        self.lookRight()
        keyboard.press("1")
        pyautogui.click(button="right")

        self.lookLeft()
        keyboard.press("2")

    def autoTorchDown(self):
        self.lookDown()
        keyboard.press("1")
        pyautogui.click(button="right")

        self.miningCameraUp()
        keyboard.press("2")

    def doNothing(self):    # This is terrible, fix later
        pass

    def miningCamera(self):
        """
        Assuming camera is looking straight ahead, re-orients camera for mining"""
        self.lookDown()
        self.miningCameraUp()

    def miningCameraUp(self):
        """
        Assuming camera is directly aimed down, moves camera to the optimal mining position
        """
        pyautogui.moveRel(0, -235, 0.5)

    def lookRight(self):
        pyautogui.moveRel(self.lookPxl, 0, 0.5)

    def lookLeft(self):
        pyautogui.moveRel(-self.lookPxl, 0, 0.5)

    def lookDown(self):
        pyautogui.moveRel(0, self.lookPxl, 0.5)

    def lookUp(self):
        pyautogui.moveRel(0, -self.lookPxl, 0.5)

def welcomeMsg():
    print("This is Jacob's simple python autominer. Press k to begin.")

# Testing purposes
if __name__ == "__main__":
    welcomeMsg()
    jacobMiner = MinerBoy()
    keyboard.wait("k")

    #####################
    #####################
    print("Program completed")


