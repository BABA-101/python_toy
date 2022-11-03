# 사용 가능 언어 출력
import pytesseract

# tesseract.exe 파일 위치
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
lang = pytesseract.get_languages(config=" ")
print(lang)
