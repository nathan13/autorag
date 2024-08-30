import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from img_processing import ImageProcessor
#python -m unittest tests/test_image_processing.py
class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        # Inicializa uma instância do ImageProcessor antes de cada teste
        self.processor = ImageProcessor(melhor_escala=1.0)
    
    @patch('img_processing.pyautogui.screenshot')
    @patch('img_processing.cv2.imread')
    def test_encontrar_imagem_OK(self, mock_imread, mock_screenshot):
        print("--------------------------------------------------------test_encontrar_imagem_OK")
        # Simulando a leitura de uma imagem
        mock_imread.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        # Simulando a captura de uma tela
        mock_screenshot.return_value = np.zeros((300, 300, 3), dtype=np.uint8)
        
        # Chame a função e verifique o resultado
        posicao = self.processor.EncontrarImagem("botao_exemplo", 0.8)
        self.assertEqual(posicao, (50, 50))  # Agora esperamos que a imagem seja encontrada na posição (50, 50)
    
    @patch('img_processing.pyautogui.screenshot')
    @patch('img_processing.cv2.imread')
    def test_encontrar_imagem_not_ERROR(self, mock_imread, mock_screenshot):
        print('--------------------------------------------------------test_encontrar_imagem_not_ERROR')
        # Simulando a leitura de uma imagem
        mock_imread.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        # Simulando a captura de uma tela com valores que não correspondem à imagem
        mock_screenshot.return_value = np.zeros((300, 300, 3), dtype=np.uint8)
        
        # Alterando o comportamento do mock para retornar um valor de correlação baixo
        with patch('img_processing.cv2.matchTemplate') as mock_match:
            mock_match.return_value = np.full((1, 1), 0.1)  # Valor de correlação baixo
            
            # Chame a função e verifique o resultado
            posicao = self.processor.EncontrarImagem("botao_exemplo", 0.8)
            self.assertIsNone(posicao)  # Agora esperamos que a imagem não seja encontrada

    @patch('img_processing.cv2.imread')
    @patch('img_processing.pyautogui.screenshot')
    @patch('img_processing.cv2.matchTemplate')
    def test_definir_escala_encontrada(self, mock_match_template, mock_screenshot, mock_imread):
        print('--------------------------------------------------------test_definir_escala_encontrada')
        # Simulando a leitura de uma imagem
        mock_imread.return_value = np.ones((100, 100, 3), dtype=np.uint8)
        
        # Simulando a captura de uma tela
        mock_screenshot.return_value = np.ones((300, 300, 3), dtype=np.uint8)
        
        # Simulando o resultado do template matching
        mock_match_template.return_value = np.full((30, 30), 0.8)  # Simula uma boa correspondência
        
        # Espera-se que a melhor escala encontrada seja 0.5
        resultado = self.processor.DefinirEscala("botao_exemplo")
        self.assertEqual(resultado, 0.5)

    @patch('img_processing.cv2.imread')
    @patch('img_processing.pyautogui.screenshot')
    @patch('img_processing.cv2.matchTemplate')
    def test_definir_escala_nao_encontrada(self, mock_match_template, mock_screenshot, mock_imread):
        print('--------------------------------------------------------test_definir_escala_nao_encontrada')
        # Simulando a leitura de uma imagem
        mock_imread.return_value = np.ones((100, 100, 3), dtype=np.uint8)
        
        # Simulando a captura de uma tela
        mock_screenshot.return_value = np.ones((300, 300, 3), dtype=np.uint8)
        
        # Simulando o resultado do template matching com baixa correlação
        mock_match_template.return_value = np.full((30, 30), 0.0)  # Simula uma correspondência ruim
        
        resultado = self.processor.DefinirEscala("botao_exemplo")
        self.assertIsNone(resultado)  # Espera-se que não encontre uma boa escala

if __name__ == '__main__':
    unittest.main()
