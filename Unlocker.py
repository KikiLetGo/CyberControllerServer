from ctypes import *
import time
# while True:
#     u = windll.LoadLibrary('user32.dll')
#     result = u.GetForegroundWindow()
#     print(result) # 0则表示锁屏
#     time.sleep(2)


import pyautogui
pyautogui.FAILSAFE=False
time.sleep(5)
pyautogui.press('enter') # enter to login.

#pyautogui.click(1025,513, 2) # click to show the password box
time.sleep(1)
pyautogui.typewrite("Asdfghjkl;'",2) # Type the password
pyautogui.press('enter') # enter to login.
time.sleep(2)

