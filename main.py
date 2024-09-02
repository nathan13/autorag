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
    limi = 0.9
    #How many tests
    tests = 3
    #'ss' = sniping shot  | 'warg' = wolf build
    build = 'warg'
    #'barao' or 'sk'
    mvp = 'barao'
    #0 = OFF | 1 = ON 
    hplock = 1
    test = 0
    #combat time "1min" or "30seg"
    combat_time = '1min'
    combat_time2 = 60

 
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
            #game_processor.Buffar('steady_focus_buff', '5')
            #game_processor.Buffar('true_sight_buff', '6')
            click_processor.FindClick('steady_focus_skill',limi)
            click_processor.FindClick('true_sight_skill',limi)

            
            #Telar para o teste        
            def littleWalk():
                pyautogui.keyDown('w')
                pyautogui.keyUp('w')

            #click_processor.FindClickWait('telar1',0.8,'telar2',0.88,'click',littleWalk)
            click_processor.FindClick('telar1',0.8)
            time.sleep(0.5)
            click_processor.FindClick('telar2',0.8)
            click_processor.FindClickWait('training_ground_button',limi,'solo_training_button',limi,'click')
            
            image_processor.WaitImage('down_arrow_button',limi,0)

            #Buffando e Escolhendo o boss
            if build == 'ss':
                click_processor.FindClick('warg_companion_skill',limi)

            click_processor.FindClickWait('down_arrow_button',limi,'mvp_challenge_button',limi,'click')
            click_processor.FindClickWait('select_mvp_button',limi,'select_mvp_image',limi,'notClick')
            maya_name = image_processor.EncontrarImagem('maya_name',limi)
            click_processor.scroll(maya_name,-900,0.5,mvp,limi)
            time.sleep(0.5)
            click_processor.FindClickWait(f'{mvp}1',limi,f'{mvp}2',limi,'notClick')

            click_processor.FindClickWait('mvp_confirm_button',limi,'restart_button',limi,'click')
            click_processor.FindClickWait('pauseAI_button',0.8,'recoverAI_button',0.8,'notClick')         
            if hplock == 1:
                click_processor.FindClickWait('hpLock_button',0.8,'cancel_hpLock_button',0.8,'notClick')

            #Iniciar o combate
            pyautogui.keyDown('w')
            time.sleep(0.7)
            pyautogui.keyUp('w')
            while True:
                pyautogui.press('k')
                combat_started_button = image_processor.EncontrarImagem('combat_started_button',0.7)
                if combat_started_button:
                    break

            pause_button_loc = image_processor.WaitImage('pause',limi,0)

            #Finalizando combate
            #image_processor.WaitImage(combat_time,0.8,0)
            image_processor.WaitImage('battle_started_image',0.8,0)
            time.sleep(combat_time2-0.5)
            click_processor.Click(pause_button_loc)
            image_processor.tirar_print('dmg2', 0.2, 'images/print_dmg.png')

            #Voltando para o inicio
            click_processor.FindClickWait('voltar1_button',limi,'voltar_confirm_button',limi,'click') 
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

            image_processor.WaitImage('escala',limi,0)
            
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
        #game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        click_processor = ClickProcessor(melhor_escala,image_processor)
        txt_processor = TextProcessor()

        #teste
        #image_processor.tirar_print('dmg2', 0.2, 'images/print_dmg.png')
        #game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        #texto = image_processor.ler_texto_imagem('print_dmg')
        click_processor.FindClickWait('down_arrow_button',limi,'mvp_challenge_button',limi,'click')
        click_processor.FindClickWait('select_mvp_button',limi,'select_mvp_image',limi,'notClick')
        maya_name = image_processor.EncontrarImagem('maya_name',limi)
        click_processor.scroll(maya_name,-900,0.5,mvp,limi)
        time.sleep(0.5)
        click_processor.FindClickWait(f'{mvp}1',limi,f'{mvp}2',limi,'notClick')
        game_processor.focar_janela('main.py - Auto Test Rag - Visual Studio Code [Administrator]')
        


        #WaitImage('30seg',0.89)

        #os.startfile('C:\Users\Nathan\Documents\programming\Python\Auto Test Rag\resultado.txt')
        
        #game_processor.focar_janela('resultado - Bloco de Notas')
        #txt_processor.salvar_texto_no_arquivo('resultado.txt', texto)
        #print(texto)

        
        #game_processor.focar_janela('images')   

if __name__ == "__main__":
    main()







