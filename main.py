"""
Gravar diarios nas pastas dos clientes
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
    

def entrar_empresa():
    # Entrar na empresa desejada
    pyautogui.click('imagens/sistema_entrar_empresa.png')
    


entrar_primavera()
pausa_tempo(15)
entrar_empresa()