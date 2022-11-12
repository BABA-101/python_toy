# folium 라이브러리 이용하여 대학교 위지 지도에 표시하기
# vworld에 접속하여 Geocoder API 2.0 레퍼런스 사용
# 포맷: http://api.vworld.kr/req/address?service=address&request=getCoord&key=인증키&[요청파라미터]
# 인증 키 발급

import requests

url='http://api.vworld.kr/req/address?'
params='service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type='ROAD' #도로명
road_type2='PARCEL' #지번
address='&address='
keys='&key='
primary_key='75AE8ECD-3956-3C76-82EF-F9FE6B9082CA'

#API에 접속하여 x,y 만 반환
def request_geo(road):
    page=requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data=page.json() #반환값은 Response 객체를 json으로 나타낸 것
    
    # print(json_data)
    
    if json_data['response']['status']=='OK':
        x=json_data['response']['result']['point']['x']
        y=json_data['response']['result']['point']['y']
        return x,y
    else:
        x=0
        y=0
        return x,y
x,y=request_geo("제주특별자치도 제주시 첨단로 242")

print(f'[*] x : {x}')
print(f'[*] x : {y}')