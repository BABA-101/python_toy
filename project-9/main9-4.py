# 번역 내용을 새 파일로 저장하는 코드
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"project-9\transText.txt"
wrtie_file_path = r"project-9\transText_KOR.txt"

with open(read_file_path, "r") as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest="ko")
    print(result1.text)

    # 파일 저장.
    # 'a' 옵션: 쓰기 위해 열기, 이미 파일이 존재하는 경우 파일 끝에 추가
    # UTF8: 한글 사용하기 위해 지정
    with open(wrtie_file_path, "a", encoding="UTF8") as f:
        f.write(result1.text + "\n")  # 한 줄 쓰고 줄바꿈
