import pyautogui
import cv2
import numpy as np
from PIL import Image,ImageFilter
import pytesseract
import re


class ImageProcessor:
    def __init__(self,melhor_escala):
        self.melhor_escala = melhor_escala

    @staticmethod
    def DefinirEscala(imagem):
        
        """Encontra a imagem em várias escalas e salva a melhor escala encontrada."""
        
        botao_original = cv2.imread(f'images/{imagem}.png')
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Define a escala mínima e máxima para redimensionar a imagem
        escala_min = 0.5
        escala_max = 1.5
        passo_escala = 0.1

        melhor_correspondencia = None
        melhor_escala = None

        for escala in np.arange(escala_min, escala_max, passo_escala):
            largura = int(botao_original.shape[1] * escala)
            altura = int(botao_original.shape[0] * escala)
            botao_redimensionado = cv2.resize(botao_original, (largura, altura))

            resultado = cv2.matchTemplate(screenshot, botao_redimensionado, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            if max_val >= 0.75 and (melhor_correspondencia is None or max_val > melhor_correspondencia):
                melhor_correspondencia = max_val
                melhor_escala = escala
                print(f"Imagem encontrada com escala {escala:.2f}, correlação: {max_val:.2f}")
                return melhor_escala

    def WaitImage(self,image,limiar):
        while True:
            imageloc = self.EncontrarImagem(image, limiar)
            if imageloc:
                break

    def EncontrarImagem(self,imagem, limi):
        """Encontra a imagem na tela usando apenas a escala salva."""
        botao_original = cv2.imread(f'images/{imagem}.png')
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Carrega a escala salva
        escala_salva = self.melhor_escala

        if escala_salva is None:
            print("Nenhuma escala salva encontrada. Execute a função DefinirEscala primeiro.")
            return None

        largura = int(botao_original.shape[1] * escala_salva)
        altura = int(botao_original.shape[0] * escala_salva)
        botao_redimensionado = cv2.resize(botao_original, (largura, altura))

        resultado = cv2.matchTemplate(screenshot, botao_redimensionado, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= limi:
            posicao_central = (max_loc[0] + largura // 2, max_loc[1] + altura // 2)
            print(max_loc, botao_original.shape[1], botao_original.shape[0])
            print(f"Imagem:'{imagem}' encontrado na posição: {posicao_central}")
            return posicao_central
        else:
            print(f"Imagem:'{imagem}' não encontrado na tela.")
            return None

    @staticmethod   
    def encontrar_print(imagem, limiar):
        """Encontra a imagem na tela e retorna a posição e tamanho da melhor correspondência encontrada."""
        # Carrega a imagem de referência
        botao_original = cv2.imread(f'images/{imagem}.png')
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        resultado = cv2.matchTemplate(screenshot, botao_original, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= limiar:
            return max_loc, botao_original.shape[1], botao_original.shape[0]
        else:
            return None, None, None  
        
    def tirar_print(self,imagem, limiar, caminho_arquivo):
        """Procura por uma imagem na tela e tira um print da região com o mesmo tamanho da imagem encontrada."""
        posicao, largura_imagem, altura_imagem = self.encontrar_print(imagem, limiar)

        if posicao:
            x, y = posicao
            # Define a região da captura com o mesmo tamanho da imagem encontrada
            screenshot = pyautogui.screenshot(region=(x, y, largura_imagem, altura_imagem))
            screenshot.save(caminho_arquivo)
            print(f"Captura salva em: {caminho_arquivo}")
        else:
            print("Imagem não encontrada na tela.")    

    @staticmethod
    def preprocessar_imagem(image):
            # Abre a imagem e converte para escala de cinza
        img = Image.open(f'images/{image}.png').convert('L')
        
        # Aplicar filtro para remover ruídos (opcional)
        img = img.filter(ImageFilter.MedianFilter())
        
        # Binarização (Thresholding)
        img = img.point(lambda x: 0 if x < 200 else 255, '1')
        
        # Opcional: Salvar a imagem preprocessada para ver o resultado
        img.save(f'images/preprocessada_{image}.png')
        img.save(f'images/imgs bug/preprocessada_{image}.png')
        
        return img

    def ler_texto_imagem(self, image):
        # Pré-processa a imagem
        img = self.preprocessar_imagem(image)
        
        # Extrai o texto da imagem
        texto_bruto = pytesseract.image_to_string(img)

        # Exibe o texto extraído
        print(f"Texto extraído: {texto_bruto.strip()}")
        
        return texto_bruto.strip()