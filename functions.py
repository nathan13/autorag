import pyautogui
import cv2
import numpy as np
import time
import os
from pywinauto import Application 
from PIL import Image,ImageFilter
import pytesseract
import os
import re

def focar_janela(titulo_janela):
    # Inicia o aplicativo (se não estiver já em execução)
    app = Application().connect(title=titulo_janela)

    # Foca na janela com o título especificado
    janela = app.window(title=titulo_janela)
    janela.set_focus()

def Buffar(image, num):
    while True:
        imageloc = EncontrarImagem(image, 0.75,melhor_escala)
        if imageloc != None:
            pyautogui.press(num)
            time.sleep(0.3)
        else:
            time.sleep(0.5)
            break

focar_janela('Ragnarok Origin: ROO')
# Executa a função para definir a escala inicial
melhor_escala = DefinirEscala('escala')