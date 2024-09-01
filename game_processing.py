
import pyautogui
import time
from pywinauto import Application 

class GameProcessor:
    def __init__(self,img_processor):
        self.img_processor = img_processor
        
    @staticmethod
    def focar_janela(titulo_janela):
        # Inicia o aplicativo (se não estiver já em execução)
        app = Application().connect(title=titulo_janela)

        # Foca na janela com o título especificado
        janela = app.window(title=titulo_janela)
        janela.set_focus()

    def Buffar(self,image, num):
        while True:
            imageloc = self.img_processor.EncontrarImagem(image, 0.75)
            if imageloc:
                pyautogui.press(num)
                time.sleep(0.5)
            else:
                break