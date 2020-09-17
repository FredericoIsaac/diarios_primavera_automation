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


def tirar_diarios(diarios, data, empresa):
    """
    Tirar diarios da empresa durante o ano todo
    """
    # Extrato diarios
    pyautogui.click('imagens/extrato_diarios.png')
    pausa_tempo(2)

    # Colocar data incial
    data_inicial_imagem = pyautogui.locateOnScreen('imagens/data_inicial.png')
    center_data_inicial = pyautogui.center(data_inicial_imagem)

    # Colocar data fim
    data_final_imagem = pyautogui.locateOnScreen("imagens/data_final.png")
    center_data_final = pyautogui.center(data_final_imagem)

    # Coloca o numero do diario           
    diarios_imagem = pyautogui.locateOnScreen('imagens/introducao_diarios.png')
    center_diarios_imagem = pyautogui.center(diarios_imagem)
    
    for diario in diarios:
        # Escrever o diario
        pyautogui.click(center_diarios_imagem.x + 188, center_diarios_imagem.y, clicks=2)
        pyautogui.write(diario)

        for mes, mes_dia in data.items():
            pyautogui.click(center_data_inicial.x + 44, center_data_inicial.y)
            # Escreve inicio do mes corrente
            pyautogui.write(mes_dia[0])

            pyautogui.click(center_data_final.x + 40, center_data_final.y)
            # Escreve final do mes corrente
            pyautogui.write(mes_dia[1])

            # Atualiza o diario
            pyautogui.click("imagens/atualizar_icnone.png")
            pausa_tempo(10)

            # Caso nao haja lançamentos no mês            
            if pyautogui.locateOnScreen('imagens/organizar_numero_doc.png') == None:
                continue

            elif diario in ("20","30","60"):
                # Organizar Lançamentos
                pyautogui.click("imagens/organizar_numero_doc.png")
                localizar_rato = pyautogui.position()
                pyautogui.click(localizar_rato[0],localizar_rato[1] + 40, button="right")
                pausa_tempo(1.5)
                pyautogui.click("imagens/organizar_ascendente.png")
                pausa_tempo(5)

            # Imprimir
            pausa_tempo(2)
            pyautogui.click("imagens/imprimir_icone.png")
            pausa_tempo(3)
            pyautogui.press("enter")
            pausa_tempo(10)
            pyautogui.click("imagens/print_pdf.png")
            pausa_tempo(2)
            pyautogui.write("{} - Extrato diario {} de {}-2019".format(empresa, diario, mes_dia[0][2:4]))
            pyautogui.press("enter")
            pausa_tempo(1)

            # Sair da janela de impressao
            extrato_impressao = pyautogui.locateOnScreen('imagens/exit_impressao_I.png')
            center_extrato_impressao = pyautogui.center(extrato_impressao)
            pyautogui.click(center_extrato_impressao.x + 733, center_extrato_impressao.y)

    
            
empresas_diarios = ["30383","10105"]

# List com o numero de diarios que se vai tirar
numero_diarios = ["20","30","40","60","61","62","71"]

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


entrar_primavera()
pausa_tempo(20)
# Create a variable to reset Primavera
count = 0

for i in range(len(empresas_diarios)):
    # Control time
    start_time = time.time()
    entrar_empresa(empresas_diarios[i])
    pausa_tempo(15)
    tirar_diarios(numero_diarios, data, empresas_diarios[i])
    print(empresas_diarios[i])
    count += 1
    # Fecha programa e volta a entrar
    if count == 3:
        pausa_tempo(2)
        pyautogui.click("imagens/reset_primavera.png")
        pausa_tempo(1)
        pyautogui.press("enter")
        pausa_tempo(20)
        entrar_primavera()
        pausa_tempo(20)
        count = 0
    print("--- %s seconds ---" % (time.time() - start_time))




