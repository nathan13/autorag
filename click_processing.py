import pyautogui
import time

class ClickProcessor:
    def __init__(self,melhor_escala,img_processor):
        self.melhor_escala = melhor_escala
        self.img_processor = img_processor

    def scroll(self,image,range,durate):
        pyautogui.moveTo(image)
        pyautogui.mouseDown()
        pyautogui.drag(0, range, duration=durate)
        pyautogui.mouseUp()
        time.sleep(1)

    def ClickWait(self,image,image2):
        while True:
            pyautogui.moveTo(image)
            pyautogui.click()

            for i in range(10):
                imageloc = self.img_processor.EncontrarImagem(image2, 0.7)
                if imageloc:
                    break
                
            if imageloc:
                return imageloc
            else:
                print(f"Imagem {image2} não encontrada")

    def FindClick(self,image,limiar):
        while True:
            image_found = self.img_processor.EncontrarImagem(image,limiar)
            if image_found:
                pyautogui.moveTo(image_found)
                pyautogui.click()
                break
            else:
                print(f"Imagem {image} não encontrada")

    def FindClickWait(self,image1,image2):
        while True:
            image1loc = self.img_processor.EncontrarImagem(image1,0.7)
            if image1loc:
                time.sleep(1)
                image2loc = self.ClickWait(image1loc,image2)
                return image2loc    
            else:
                print(f"Imagem {image1} não encontrada")

    def Click(self,image):
        pyautogui.moveTo(image)
        pyautogui.click()