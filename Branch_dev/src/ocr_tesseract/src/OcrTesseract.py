import pytesseract
import numpy as np
import cv2
class OcrTesseract:
    def __init__(self, image_path):
        self._ImagePath = image_path
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def execute(self):
        #for windows only
        img = cv2.cvtColor(cv2.imread(self._ImagePath), cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img)