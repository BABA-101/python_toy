# 이미지에서 한글 찾아서 추출하는 코드 만들기
from PIL import Image
import pytesseract

image_path=r'project-22\kor_img.png'

# tesseract.exe 파일 위치
pytesseract.pytesseract.tesseract_cmd=r''
text=pytesseract.image_to_string(Image.open(image_path),iang="kor")

print(text)