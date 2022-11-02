from PIL import Image
import pytesseract

image_path=r'project-22\kor_img.png'

# tesseract.exe 파일 위치
pytesseract.pytesseract.tesseract_cmd=r''
text=pytesseract.image_to_string(Image.open(image_path),lang='kor')

print(text)

with open(r'project-22\kor_conv.txt',"w",encoding="urf-8") as f:
    f.write(text)