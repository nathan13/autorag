
import pyautogui
import time
from pywinauto import Application 
import img_processing


def focar_janela(titulo_janela):
    # Inicia o aplicativo (se não estiver já em execução)
    app = Application().connect(title=titulo_janela)

    # Foca na janela com o título especificado
    janela = app.window(title=titulo_janela)
    janela.set_focus()

def Buffar(image, num):
    from main import melhor_escala
    while True:
        imageloc = img_processing.EncontrarImagem(image, 0.75,melhor_escala)
        if imageloc != None:
            pyautogui.press(num)
            time.sleep(0.3)
        else:
            time.sleep(0.5)
            break