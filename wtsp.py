import pyautogui as gui
import time
message = input("enter the messege ")
number = input("enter the number ")
time.sleep(20)
for i in range(int(number)):
  gui.typewrite(message)
  gui.press('Enter')