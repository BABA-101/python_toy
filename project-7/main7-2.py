from currency_converter import CurrencyConverter

cc=CurrencyConverter()
# USD 1달러를 대한민국 원화로 변경 시 얼마인가?
print(cc.convert(1,'USD','KRW'))