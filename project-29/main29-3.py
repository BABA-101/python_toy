import streamlit as st
import datetime
import pyupbit

d=st.date_input("날짜 선택",datetime.date.today())

st.write('BTC 1일 차트')

# 비트코인 60분짜리 데이터 24개
ticker='KRW-BTC'
interval='minute60' #60분봉
to=str(d+datetime.timedelta(days=1))
count=24

# 입력한 날짜에 하루 더하기
# get_ohlcv(): 어떤 코인의 과거 가격 내역을 조회
# 하루를 더하는 이유는, 과거 내역을 가져오는 것이기 때문에.. 입력 날짜의 데이터를 가져오려면 하루 더한 후 get_ohlcv()를 사용해야 함.
price_now=pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

# 차트 그려
# 시가(open), 고가(high), 저가(low), 종가(close), 거래량(volume)
# price_now 하면 모두 나옴.
st.line_chart(price_now.close)
