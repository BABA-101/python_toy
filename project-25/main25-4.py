# 특정 기간동안의 비트코인 데이터 읽어서 DB에 저장
import pyupbit
import sqlite3
import datetime

# datetime 라이브러리 이용하여 시작날짜와 종료날짜 모든 날을 리스트 형태로 반환
def date_range(start,end):
    # strptime(): 다양한 포맷의 문자열을 datetime 객체로 변환
    # datetime.strptime(문자열, 형식)
    start=datetime.datetime.strptime(start,"%Y-%m-%d")
    # datetime.timedelta(days=1) 하루를 의미, 즉, 이 부분에서는 start가 start의 다음날이 된다.
    # 1일을 더하는 이유는 해당 날짜 데이터를 얻기 위해. (이유는 11월 30일의 데이터를 모으기 위해서는 12월 1일 00시00분 이전 하루치 데이터를 모으기 위해)
    start=start+datetime.timedelta(days=1)
    end=datetime.datetime.strptime(end,"%Y-%m-%d")
    # 마찬가지로 12월 1일까지 데이터를 모으고 싶다면, 12월2일 00시00분 이전의 하루치 데이터를 불러와야 하기 때문
    end=end+datetime.timedelta(days=1)
    dates=[(start+datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates=date_range("2021-11-30","2021-12-01")

print(dates)

# 날짜 뒤집기. 최신 날짜로부터 과거로 데이터를 수집하기 때문이다.
for day in reversed(dates):
    myDay=day+' 00:00'
    print(myDay)

    # 하루치 분봉 데이터 요청, 하루 24시간 * 60분 = 1440분
    ticker='KRW-BTC'
    interval='minute1'
    to=myDay
    count=1440
    price_now=pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

    print(price_now)
    
    db_path=r'project-25\coin.db'

    con=sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC',con,if_exists='append')

    con.close