import pyautogui
import time
from click_processing import ClickProcessor
from img_processing import ImageProcessor
from txt_processing import TextProcessor
from game_processing import GameProcessor
import os


def main():
#PRESETS
    #limiar padrao
    limi = 0.7
    #How many tests
    tests = 2
    #1 = SNIPING | 2 = WOLF
    build = 2
    #0 = OFF | 1 = ON 
    hplock = 1
    test = 0
    #combat time
    combat_time = 60

 
 #Inicio
    if test == 0: 
        #Criando instancias e definindo escala padrao
        GameProcessor.focar_janela('Ragnarok Origin: ROO')
        melhor_escala = ImageProcessor.DefinirEscala('escala')
        image_processor = ImageProcessor(melhor_escala)
        game_processor = GameProcessor(image_processor)
        click_processor = ClickProcessor(melhor_escala,image_processor)
        txt_processor = TextProcessor()
  
        for i in range(tests) :
            #Buffs iniciais
            game_processor.Buffar('buff1', '5')
            game_processor.Buffar('buff2', '6')

            #Telar para o teste
            telar2 = click_processor.FindClickWait('telar1','telar2')
            telar3 = click_processor.ClickWait(telar2,'telar3')
            telar4 = click_processor.ClickWait(telar3,'telar4')
            click_processor.Click(telar4)
            image_processor.WaitImage('mvp1',0.65)

            #Buffando e Escolhendo o boss
            if build == 1:
                game_processor.Buffar('buff3', '2')

            mvp2 = click_processor.FindClickWait('mvp1','mvp2')
            mvp3 = click_processor.ClickWait(mvp2,'mvp3')
            mvp4 = click_processor.ClickWait(mvp3,'mvp4')
            while True:
                click_processor.scroll(mvp4,-900,0.5)
                barao = image_processor.EncontrarImagem('barao1',0.7)
                if barao != None:
                    break
            click_processor.Click(barao)
            mvp9 = click_processor.FindClickWait('mvp8','mvp9')
            click_processor.Click(mvp9)
            click_processor.FindClick('mvp10',0.7)
            if hplock == 1:
                click_processor.FindClick('hplock',0.7)

            #Iniciar o combate
            pyautogui.keyDown('w')
            time.sleep(0.7)
            pyautogui.keyUp('w')
            pyautogui.press('k')
            image_processor.WaitImage("dmg",0.2)
            time.sleep(combat_time + 0.7)
            #WaitImage('30seg',0.89)

            #Finalizando combate
            click_processor.FindClick('pause',0.7)
            time.sleep(0.5)
            image_processor.tirar_print('dmg', 0.2, 'images/print_dmg.png')

            #Voltando para o inicio
            voltar2 = click_processor.FindClickWait('voltar1','voltar2')
            click_processor.Click(voltar2)

            texto = image_processor.ler_texto_imagem('print_dmg')
            txt_processor.salvar_texto_no_arquivo('resultado.txt', texto)

            # Lê os valores dos testes
            valores = txt_processor.ler_testes_arquivo('resultado.txt')
            
            # Total de testes
            total_testes = len(valores)
            
            if valores:
                # Calcula as estatísticas
                media, maior_valor, menor_valor = txt_processor.calcular_estatisticas(valores)
                
                # Encontra os testes com maior e menor valor
                maior_teste, menor_teste = txt_processor.encontrar_testes_maior_menor(valores)
                
                # Atualiza o arquivo com as informações
                txt_processor.atualizar_arquivo('resultado.txt', total_testes, media, maior_valor, menor_valor, maior_teste, menor_teste)

            
            image_processor.WaitImage('escala',0.65)
        print(f"Tests Performed: {tests}\nEnd------------------------------------------------------------------------------")
        os.startfile('C:/Users/Nathan/Documents/programming/Python/Auto Test Rag/resultado.txt')
        game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        game_processor.focar_janela('resultado - Bloco de Notas')
    else:
        #Criando instancias e definindo escala padrao
        GameProcessor.focar_janela('Ragnarok Origin: ROO')
        melhor_escala = ImageProcessor.DefinirEscala('escala')
        image_processor = ImageProcessor(melhor_escala)
        game_processor = GameProcessor(image_processor)
        game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        click_processor = ClickProcessor(melhor_escala,image_processor)
        txt_processor = TextProcessor()

        #teste
        #image_processor.tirar_print('dmg', 0.2, 'images/print_dmg.png')
        texto = image_processor.ler_texto_imagem('print_dmg')
        #os.startfile('C:\Users\Nathan\Documents\programming\Python\Auto Test Rag\resultado.txt')
        #game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        #game_processor.focar_janela('resultado - Bloco de Notas')
        #txt_processor.salvar_texto_no_arquivo('resultado.txt', texto)
        print(texto)

        
        #game_processor.focar_janela('images')   

if __name__ == "__main__":
    main()







