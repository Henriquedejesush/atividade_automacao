import pyautogui
import time
import getpass

# def espera(segundos=2):
#     time.sleep(segundos)


# def clique(x,y,delay=2):
#     espera(delay)
#     pyautogui.click(x = x, y = y)



# def dois_cliques(x,y,delay=2):
#     espera(delay)
#     pyautogui.doubleClick(x = x, y = y)


# def abrir_site(nome_site, delay=2):
#     espera(delay)
#     pyautogui.write(nome_site)  # <-- Corrigido
#     espera(delay)
#     pyautogui.press("enter")
#     espera(1)



# clique(1805,31)
# dois_cliques(86, 623)
# abrir_site("https://www.to.senac.br/")
# clique(563,708)
# clique(528, 876)


def espera(segundos = 2):
    time.sleep(segundos)


def clique1(x,y,delay=2):
    espera(delay)
    pyautogui.click(x = x, y = y)
    

def dois_cliques2(x,y,delay=2):
    espera(delay)
    pyautogui.doubleClick(x = x, y = y)

def abrir_site2(nome_site,delay=2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press("enter")
    espera(1)

def colocar_email(nome_email,delay=2):
    espera(delay)
    pyautogui.write(nome_email)
    espera(delay)
    pyautogui.press("enter")
    espera(1)

def colocar_senha(senha_login,delay=2):
    espera(delay)
    pyautogui.write(senha_login)
    espera(delay)
    pyautogui.press("enter")
    espera(1)

senha = getpass.getpass("Digite sua senha: ")

def enviar_email(email_destino,delay=2):
    espera(delay)
    pyautogui.write(email_destino)
    espera(delay)
    pyautogui.press("enter")


def assunto_tarefa(assunto,delay=2):
    espera(delay)
    pyautogui.write(assunto)
    espera(delay)
   
 


clique1(1805,31) # Minimizar vs code
dois_cliques2(86, 623) # Abrir o chrome
abrir_site2("https://workspace.google.com/intl/pt-BR/gmail/") # Colocar o nome do site
clique1(1648, 113) # clicar em fazer login
colocar_email("seuemail@gmail.com") # Inserir o email
colocar_senha(senha) # inserir senha
clique1(36, 111) # Clicar nas 3 barrinhas
clique1(35, 180) # Clicar em em opcao de enviar email
enviar_email("mateusgm@to.senac.pr") # Colocar email de destino
clique1(1289, 521) # Clicar no assunto
assunto_tarefa("Boa noite, Professor! Te mandei os exercicios que fiz, espero que fique feliz. (:")
clique1(1423, 998) # Abrir o explore para fazer o envio de arquivos
clique1(89, 257) # Abrir pasta documentos
dois_cliques2(514, 241)
dois_cliques2(488, 186)
clique()







