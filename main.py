import keyboard
import pyautogui
import time
import threading

class MinerBoy():     

    @staticmethod
    def turnRight():
        for _ in range (4):
            pyautogui.move(1000, 0)

    @staticmethod
    def turnLeft():
        for _ in range (4):
            pyautogui.move(-1000, 0)

    def __init__(self, miningCylces):
        self.currentlyWalking = False
        self.currentlyTunneling = False
        self.escapeKey = "s"
        self.cyclesRemaining = miningCylces
        self.continueMining = True

    def mine(self):
        threading.Timer(1, self.checkEndMining).start()

        while self.cyclesRemaining > 0 and self.continueMining:
            self.toggleShiftWalk()
            self.toggleTunnel()
            time.sleep(10)
            self.toggleShiftWalk()
            self.toggleTunnel()
            MinerBoy.autoTorch()
            self.cyclesRemaining -= 1

    def checkEndMining(self):
        
        while self.cyclesRemaining > 0:
            print("checking.......")
            if keyboard.is_pressed(self.escapeKey):
                self.continueMining = False
                print("Mining stopping at next cycle")
                break
            else:
                time.sleep(2)

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
    jacobMiner = MinerBoy(3)
    keyboard.wait("k")
    jacobMiner.mine()
    
    print("Program completed")

main()


