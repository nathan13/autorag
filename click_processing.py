import pyautogui
import time

class ClickProcessor:
    def __init__(self,melhor_escala,img_processor):
        self.melhor_escala = melhor_escala
        self.img_processor = img_processor

    def scroll(self,image,range,durate,mvp,limi):
        while True:
            pyautogui.moveTo(image)
            pyautogui.mouseDown()
            pyautogui.drag(0, range, duration=durate)
            pyautogui.mouseUp()
            bossloc = self.img_processor.EncontrarImagem(f'{mvp}1',limi)
            if bossloc:
                break
 
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

    def FindClickWait(self,image1,limi1,image2,limi2,action,func = None):
        while True:
            self.FindClick(image1,limi1)
            image2loc = self.img_processor.WaitImage(image2,limi2,10)
            if image2loc:
                if action == 'click':
                    self.Click(image2loc) 
                break
            elif func:
                func()

    def Click(self,image):
        pyautogui.moveTo(image)
        pyautogui.click()