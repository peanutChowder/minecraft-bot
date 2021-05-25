import keyboard
import pyautogui
import time

class MinerBoy():     

    @staticmethod
    def turnRight():
        for _ in range (4):
            pyautogui.move(1000, 0)

    @staticmethod
    def turnLeft():
        for _ in range (4):
            pyautogui.move(-1000, 0)

    def __init__(self):
        self.currentlyWalking = False
        self.currentlyMining = False
        self.escapeMiner = False

    def toggleShiftWalk(self):
        if self.currentlyWalking:
            keyboard.release("shift")
            keyboard.release("w")
        else:
            keyboard.press("shift")
            keyboard.press("w")
        self.currentlyWalking = not self.currentlyWalking

    def toggleMine(self):
        if self.currentlyMining:
            pyautogui.mouseUp()
        else:
            pyautogui.mouseDown()
        self.currentlyMining = not self.currentlyMining

    def autoTorch():
        MinerBoy.turnRight()
        keyboard.press("1")
        pyautogui.click(button="right")
        MinerBoy.turnLeft()
        keyboard.press("2")

def welcomeMsg():
    print("This is Jacob's simple python autominer. Press k to begin.")



def main():
    welcomeMsg()
    jacobMiner = MinerBoy()
    keyboard.wait("k")
    for _ in range(10):
        if keyboard.is_pressed("s"):
            break
        jacobMiner.toggleShiftWalk()
        jacobMiner.toggleMine()
        time.sleep(10)
        jacobMiner.toggleShiftWalk()
        jacobMiner.toggleMine()
        MinerBoy.autoTorch()
    

    # Delete below
    print("done")

main()


