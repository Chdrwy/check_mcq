from src.OcrTesseract import OcrTesseract
import os

ot = OcrTesseract(os.getcwd()+'/../utils/image.png')
text = ot.execute()
