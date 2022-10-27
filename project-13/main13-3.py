# 사이트에서 이메일을 수집
import requests
import re

# 수집할 사이트
url='https://www.news1.kr/articles/?4846342&kakao_from=mainnews'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

res=requests.get(url,headers=headers)

results=re.findall(r'[\w\.-]+@[\w\.-]+',res.text)
results=list(set(results))
print(results)