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

# List com o numero de diarios que se vai tirar
numero_diarios = [10,20,30,40,60,61,62,63,71]

# Dict com as datas do inicio do mes e fim de 2019
data = {
    "janeiro": ["01012019","31012019"],
    "fevereiro": ["01022019","29022019"],
    "março": ["01032019","31032019"],
    "abril": ["01042019","30042019"],
    "maio": ["01052019", "31052019"],
    "junho": ["01062019", "30062019"],
    "julho": ["01072019", "31072019"],
    "agosto": ["01082019", "31082019"],
    "setembro": ["01092019", "30092019"],
    "outubro": ["01102019", "31102019"],
    "novembro": ["01112019", "30112019"],
    "dezembro": ["01122019", "31122019"]
}



def tirar_diarios(diarios):
    """
    Tirar diarios da empresa durante o ano todo
    """
    # Extrato diarios
    pyautogui.click('imagens/extrato_diarios.png')
    pausa_tempo(2)

    # Colocar data incial
    data_inicial_imagem = pyautogui.locateOnScreen('imagens/data_inicial.png')
    center_data_inicial = pyautogui.center(data_inicial_imagem)
    data_inicial = pyautogui.click(center_data_inicial.x + 44, center_data_inicial.y)

    # Colocar data fim
    data_final_imagem = pyautogui.locateOnScreen("imagens/data_final.png")
    center_data_final = pyautogui.center(data_final_imagem)
    data_final = pyautogui.click(center_data_final.x + 40, center_data_final.y)

    for diario in numero_diarios:
        for mes, mes_dia in data.items():
            data_inicial
            # Escreve inicio do mes corrente
            pyautogui.write(mes_dia[0])
            data_final
            # Escreve final do mes corrente
            pyautogui.write(mes_dia[1])
            pausa_tempo(0.5)

    


tirar_diarios(numero_diarios)
