import pyautogui
import time

time.sleep(3)
pyautogui.click(x=1803, y=25)
time.sleep(2)
pyautogui.doubleClick(x=86, y=623)
time.sleep(1)
pyautogui.write("https://accounts.google.com/")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("seuemail@gmail.com")
time.sleep(1)
pyautogui.click(x=1394, y=674)
time.sleep(1)
pyautogui.write("lindodemais")
time.sleep(1)
pyautogui.click(x=1401, y=658)
