# 비트코인 분봉 데이터 데이터베이스에 저장
import sqlite3
import pyupbit

# 한화로 비트코인 데이터 불러오기, 분봉으로, to 이전의 데이터, 200개
ticker='KRW-BTC'
interval='minute1'
to='2021-12-02 11:20'
count=200
# 값은 데이터프레임 형식으ㅡ로 반환
price_now=pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

db_path=r'project-25\coint.db'
# DB생성
# isolation_level: 트랜잭션의 격리 수준. 
# 특정 트랜잭션이 다른 트랜잭션에 변경한 데이터를 볼 수 있도록 허용할지 유무
# 해당 옵션 통해 현재의 기본 격리 수준을 가져오거나 설정, None은 자동 커밋 모드
con=sqlite3.connect(db_path,isolation_level=None)
# BTC의 이름으로 데이터 생성 후 데이터 추가
price_now.to_sql('BTC',con,if_exists='append')

con.close
