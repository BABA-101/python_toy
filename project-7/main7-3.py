# 실시간 환율 정보 크롤링 코드
import requests
#BeautifulSoup: HTML과 XML 문서 구문을 깔끔하게
from bs4 import BeautifulSoup

def get_exchange_rate(target1,target2):
    #헤더 없이 접속면 로봇이 접속한 것으로 확인하여 사이트에서 정보를 주지 않음.
    headers = {
        'User-Agent':'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    #응답값 가져오기
    response=requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1,target2),headers=headers)
    
    #BeautifulSoup 라이브러리 이용하여 html 가독성 상승
    content = BeautifulSoup(response.content,'html.parser')
    
    #마지막 환율 정보 가져오기
    containers=content.find('태그',{'속성':'값'})
    print(containers.text)


get_exchange_rate('usd','krw')
