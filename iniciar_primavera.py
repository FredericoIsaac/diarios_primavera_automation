"""
Abrir Primavera e inicias com a empresa desejada
"""

import pyautogui
import time

def pausa_tempo(segundos):
    """
    Input numero de segundos para fazer pausa 
    """
    return time.sleep(segundos)

def entrar_primavera():
    """
    Fazer Login no Primavera
    """
    # Click no icone primavera na barra de tarefas 
    pyautogui.click('imagens/icon_primavera.png')
    pausa_tempo(3)
    # Login primavera
    pyautogui.write("962209")
    pyautogui.press('enter')
    

def entrar_empresa(empresa):
    """
    Vai abrir listagem de empresas e entrar na empresa do input
    """
    # Entrar na empresa desejada
    pyautogui.click('imagens/sistema_entrar_empresa.png')
    pausa_tempo(1)
    # Abrir empresa
    pyautogui.click('imagens/abrir_empresa.png')
    pausa_tempo(3)
    # Abrir listagem empresa
    pyautogui.click('imagens/listagem_empresas.png')
    pausa_tempo(0.5)
    # Abrir listagem de todas as empresa
    pyautogui.click('imagens/listagem_empresas_todas.png')
    pausa_tempo(1)
    pyautogui.write(empresa)
    pyautogui.press('enter')


    

# empresa = input("Insira a empresa desejada: ")
# entrar_primavera()
# pausa_tempo(15)
# entrar_empresa(empresa)
# pausa_tempo(20)
numero_diarios = [10,20,30,40,60,61,62,63,71]
data = {
    "janeiro": ["01012019","31012019"],
    "fevereiro": ["01022019","29022019"],
    "março": ["01032019","31032019"],
    "abril": ["01042019","30042019"],
    "maio"
}
def tirar_diarios(numero_diarios):
    """
    Tirar diarios da empresa durante o ano todo
    """
    # Extrato diarios
    pyautogui.click('imagens/extrato_diarios.png')
    pausa_tempo(3)
    # Colocar data incial
    data_inicial = pyautogui.locateOnScreen('imagens/data_inicial.png')
    center_data_inicial = pyautogui.center(data_inicial)
    pyautogui.click(center_data_inicial.x + 44, center_data_inicial.y)
    pyautogui.write("31012020")


tirar_diarios(10)