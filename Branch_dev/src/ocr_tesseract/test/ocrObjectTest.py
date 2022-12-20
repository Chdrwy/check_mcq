from src.OcrTesseract import OcrTesseract

ot = OcrTesseract('')
if not isinstance(ot, OcrTesseract):
    print('Object is not instance of ocrTesseract')