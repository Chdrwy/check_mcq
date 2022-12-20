from src.OcrTesseract import OcrTesseract
from src.DownloadHttpImage import DownloadHttpImage
import os

#downloading some image to test ocr using tesseract
di = DownloadHttpImage('https://jeroen.github.io/images/testocr.png')
filename = di.download(os.getcwd())

#starting instanceof OcrTesseract that will use tesseract to convert image to character
#using optical character recognition - OCR
ot = OcrTesseract(os.getcwd()+'/'+filename)
text = ot.execute()
