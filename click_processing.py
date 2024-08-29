import pyautogui
import time
import img_processing

class ClickProcessor:
    def __init__(self,melhor_escala):
        self.melhor_escala = melhor_escala

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
            time.sleep(0.2)

            for i in range(10):
                imageloc = img_processing.EncontrarImagem(image2, 0.7,self.melhor_escala)
                if imageloc:
                    break
                time.sleep(0.5)
            if imageloc:
                return imageloc

    def FindClick(self,image):
        image_found = img_processing.EncontrarImagem(image,0.7,self.melhor_escala)
        pyautogui.moveTo(image_found)
        pyautogui.click()

    def FindClickWait(self,image1,image2):
        while True:
            image1loc = img_processing.EncontrarImagem(image1,0.7,self.melhor_escala)
            image2loc = self.ClickWait(image1loc,image2)
            return image2loc    

    def ClickWait(self,image,image2):
        while True:
            pyautogui.moveTo(image)
            pyautogui.click()
            time.sleep(0.2)

            for i in range(10):
                imageloc = img_processing.EncontrarImagem(image2, 0.7,self.melhor_escala)
                if imageloc:
                    break
            if imageloc:
                return imageloc

    def Click(self,image):
        pyautogui.moveTo(image)
        pyautogui.click()