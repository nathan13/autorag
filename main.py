import pyautogui
import time
from pywinauto import Application 
import txtProcessing
import imgProcessing
import clickProcessing

def focar_janela(titulo_janela):
    # Inicia o aplicativo (se não estiver já em execução)
    app = Application().connect(title=titulo_janela)

    # Foca na janela com o título especificado
    janela = app.window(title=titulo_janela)
    janela.set_focus()

def Buffar(image, num):
    while True:
        imageloc = imgProcessing.EncontrarImagem(image, 0.75,melhor_escala)
        if imageloc != None:
            pyautogui.press(num)
            time.sleep(0.3)
        else:
            time.sleep(0.5)
            break

#PRESETS
#1 = SNIPING | 2 = WOLF
build = 2
#0 = OFF | 1 = ON 
hplock = 1
test = 1
#Inicio
#Definir a escala padrao
focar_janela('Ragnarok Origin: ROO')
melhor_escala = imgProcessing.DefinirEscala('escala')

if test == 0:   
    while True:
        #Buffs iniciais
        Buffar('buff1', '5')
        Buffar('buff2', '6')

        #Telar para o teste
        telar2 = clickProcessing.FindClickWait('telar1','telar2')
        telar3 = clickProcessing.ClickWait(telar2,'telar3')
        telar4 = clickProcessing.ClickWait(telar3,'telar4')
        clickProcessing.Click(telar4)
        time.sleep(2)
        imgProcessing.WaitImage('escala',0.65)

        #Buffando e Escolhendo o boss
        if build == 1:
            Buffar('buff3', '2')
        elif build == 2:
            Buffar('buff4', '1')
        
        mvp2 = clickProcessing.FindClickWait('mvp1','mvp2')
        mvp3 = clickProcessing.ClickWait(mvp2,'mvp3')
        mvp4 = clickProcessing.ClickWait(mvp3,'mvp4')
        while True:
            clickProcessing.scroll(mvp4,-900,0.5)
            time.sleep(1)
            barao = imgProcessing.EncontrarImagem('barao1',0.7,melhor_escala)
            if barao != None:
                break
        clickProcessing.Click(barao)
        mvp9 = clickProcessing.FindClickWait('mvp8','mvp9')
        clickProcessing.Click(mvp9)
        clickProcessing.FindClick('mvp10')
        if hplock == 1:
            clickProcessing.FindClick('hplock')

        #Iniciar o combate
        pyautogui.keyDown('w')
        time.sleep(0.7)
        pyautogui.keyUp('w')
        pyautogui.press('k')
        time.sleep(60.2)
        #WaitImage('30seg',0.89)

        #Finalizando combate
        clickProcessing.FindClick('pause')
        time.sleep(0.5)
        imgProcessing.tirar_print('dmg', 0.7, 'images/print_dmg.png')
        imgProcessing.tirar_print('dps', 0.65, 'images/print_dps.png')
        texto = imgProcessing.ler_texto_imagem('print_dmg')
        txtProcessing.salvar_texto_no_arquivo('resultado.txt', texto)

        # Lê os valores dos testes
        valores = txtProcessing.ler_testes_arquivo('resultado.txt')
        
        # Total de testes
        total_testes = len(valores)
        
        if valores:
            # Calcula as estatísticas
            media, maior_valor, menor_valor = txtProcessing.calcular_estatisticas(valores)
            
            # Encontra os testes com maior e menor valor
            maior_teste, menor_teste = txtProcessing.encontrar_testes_maior_menor(valores)
            
            # Atualiza o arquivo com as informações
            txtProcessing.atualizar_arquivo('resultado.txt', total_testes, media, maior_valor, menor_valor, maior_teste, menor_teste)

        #Voltando para o inicio
        voltar2 = clickProcessing.FindClickWait('voltar1','voltar2')
        clickProcessing.Click(voltar2)
        time.sleep(2)
        imgProcessing.WaitImage('escala',0.65)
else:
    #teste
    import logging
    botao_original = None
    logging.warning(f"Imagem de aaaa não encontrada")
    if not botao_original:
        print('vazio')
        
    focar_janela('test.py - Auto Test Rag - Visual Studio Code [Administrator]')








