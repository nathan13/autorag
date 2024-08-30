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
            time.sleep(0.2)

            for i in range(10):
                imageloc = self.img_processor.ImageProcessor.EncontrarImagem(image2, 0.7)
                if imageloc:
                    break
                time.sleep(0.5)
            if imageloc:
                return imageloc

    def FindClick(self,image):
        image_found = self.img_processor.EncontrarImagem(image,0.7,)
        pyautogui.moveTo(image_found)
        pyautogui.click()

    def FindClickWait(self,image1,image2):
        while True:
            image1loc = self.img_processor.EncontrarImagem(image1,0.7)
            image2loc = self.ClickWait(image1loc,image2)
            return image2loc    

    def ClickWait(self,image,image2):
        while True:
            pyautogui.moveTo(image)
            pyautogui.click()
            time.sleep(0.2)

            for i in range(10):
                imageloc = self.img_processor.EncontrarImagem(image2, 0.7)
                if imageloc:
                    break
            if imageloc:
                return imageloc

    def Click(self,image):
        pyautogui.moveTo(image)
        pyautogui.click()