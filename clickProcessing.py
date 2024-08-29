import pyautogui
import time
import imgProcessing
from main import melhor_escala

def scroll(image,range,durate):
    pyautogui.moveTo(image)
    pyautogui.mouseDown()
    pyautogui.drag(0, range, duration=durate)
    pyautogui.mouseUp()
    time.sleep(1)

def ClickWait(image,image2):
    while True:
        pyautogui.moveTo(image)
        pyautogui.click()
        time.sleep(0.2)

        for i in range(10):
            imageloc = imgProcessing.EncontrarImagem(image2, 0.7,melhor_escala)
            if imageloc:
                break
            time.sleep(0.5)
        if imageloc:
            return imageloc

def FindClick(image):
    image_found = imgProcessing.EncontrarImagem(image,0.7,melhor_escala)
    pyautogui.moveTo(image_found)
    pyautogui.click()

def FindClickWait(image1,image2):
    while True:
        image1loc = imgProcessing.EncontrarImagem(image1,0.7,melhor_escala)
        image2loc = ClickWait(image1loc,image2)
        return image2loc    

def ClickWait(image,image2):
    while True:
        pyautogui.moveTo(image)
        pyautogui.click()
        time.sleep(0.2)

        for i in range(10):
            imageloc = imgProcessing.EncontrarImagem(image2, 0.7,melhor_escala)
            if imageloc:
                break
        if imageloc:
            return imageloc

def Click(image):
    pyautogui.moveTo(image)
    pyautogui.click()