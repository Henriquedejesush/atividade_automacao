import pyautogui
import time
import os

email = "seuemail@gmail.com"
senha = os.getenv("SENHA_GMAIL")  # Defina antes no sistema

time.sleep(3)
pyautogui.click(x=1803, y=25)  # Abre navegador
time.sleep(2)
pyautogui.doubleClick(x=86, y=623)  # Barra de endereços
time.sleep(1)
pyautogui.write("https://accounts.google.com/")
pyautogui.press("enter")
time.sleep(5)  # Aguarda página carregar

pyautogui.write(email)
time.sleep(1)
pyautogui.click(x=1394, y=674)  # Próxima
time.sleep(2)

pyautogui.write(senha)
time.sleep(1)
pyautogui.click(x=1401, y=658)  # Próxima
