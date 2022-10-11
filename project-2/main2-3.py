import requests
import re  # 정규표현식 모듈

req = requests.get("http://ipconfig.kr")

# 정규표현식 표현. \d는 숫자를 의미
# \d{1,3}은 숫자가 1개 또는 2개 있어야 함.
# search(패턴, 문자열, 플래그), 패턴과 일치하면 전부 찾아서 반환해준다.
# req.text: 홈페이지 코드 다긁어옴
out_addr = re.search(r"IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1]
print(out_addr)
