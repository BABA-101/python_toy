#pyupbit: 업비트에서 가상화폐 데이터를 조회할 수 있는 라이브러리
#가상화폐 시세조회 코드
import pyupbit

#get_tickers: 암호화폐 티커 조회, fiat=거래기준화폐
coin_lists=pyupbit.get_tickers(fiat='KRW')
print(coin_lists)

#비트코인과 이더리움 한국 시세 출력
price_now=pyupbit.get_current_price(["KRW-BTC","KRW-ETH"])
print(price_now)