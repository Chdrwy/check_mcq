from src.DownloadHttpImage import DownloadHttpImage
import os

di = DownloadHttpImage('https://jeroen.github.io/images/testocr.png')
di.download(os.getcwd()+'/image.png')