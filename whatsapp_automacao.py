import os 
os.system("cls")
import openpyxl # Biblioteca pra trablhar com planilhas tipo excel
from datetime import datetime
from urllib.parse import quote # Nessa serve pra decodificar a url
import webbrowser
from time import sleep
import pyautogui
import sys

webbrowser.open("https://web.whatsapp.com/")
sleep (10)

workbook = openpyxl.load_workbook("Numeros2.xlsx")
pagina_cliente = workbook["Plan1"]

for linha in pagina_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    numero = linha[1].value
    status = linha[2].value
    data = linha[3].value

    if nome is None or numero is None:
        break

    data = "2025-05-23"  # formato ISO (aaaa-mm-dd)
    data = datetime.strptime(data, '%Y-%m-%d')
    data = data.strftime('%d/%m/%Y')

    mensagem = f"Olá {nome}, Você tem contas a pagar desde o dia {data}!"

    link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={numero}&text={quote(mensagem)}"
    webbrowser.open(link_mensagem_whatsapp)

    sleep(10)

    def um_clique(x,y):
        pyautogui.click(x = x, y = y)
        sleep(5)

    um_clique(1721, 976)
    sleep(5)
    um_clique(504, 12)
    sleep(5)

sys.exit()

    