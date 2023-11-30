import pytesseract as tess
tess.pytesseract.tesseract_cmd = (r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
from PIL import Image

img = Image.open (r"C:\\Users\\sdndu\\Documents\\TUGAS KAMPUS ZEIN SMT 3\\PBO\\per 7\\new 7\\zein.png")
text = tess.image_to_string (img)

print (text)