# 사용 가능 언어 출력
import pytesseract 

# tesseract.exe 파일 위치
pytesseract.pytesseract.tesseract_cmd=r''
lang=pytesseract.get_languages(config=' ')
print(lang)