import pyautogui as pt
import time, sys

def mine_block(seconds):
    pt.mouseDown(button="left")
    time.sleep(seconds)
    pt.mouseUp(button="left")

pickaxe = str(input("What pickaxe do you have? (wood, stone, iron, gold, diamond, netherite)? "))

if pickaxe == "gold" or pickaxe == "Gold" or pickaxe == "GOLD":
    pickaxe_mining_time = 25
else:
    print("Please use a Gold Pickaxe ;)")
    sys.exit()

picaxes = int(input("How many Picaxes do you currently have in your Inventory? "))

time.sleep(10)
print("Time to MINE!!")

for i in range(1, pickaxes+1):
    pt.press(str(i))
    mine_block(pickaxe_mining_time)
