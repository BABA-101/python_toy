# 당첨번호 빈도수 출력하는 코드
import pandas as pd
from collections import Counter

file_path=r'project-26\lotto.xlsx'
df_from_excel=pd.read_excel(file_path,engine='openpyxl')

df_from_excel=df_from_excel.drop(index=[0,1])

df_from_excel.columns=[
    '년도','회차','추첨일','1등당첨자수',
    '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
    '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
    '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
    '당첨번호4','당첨번호5','당첨번호6','보너스번호'
]

# 6개의 번호를 인트형으로 읽어 num_list에 더해줌
num_list=list(df_from_excel['당첨번호1'].astype(int))
num_list+=list(df_from_excel['당첨번호2'].astype(int))
num_list+=list(df_from_excel['당첨번호3'].astype(int))
num_list+=list(df_from_excel['당첨번호4'].astype(int))
num_list+=list(df_from_excel['당첨번호5'].astype(int))

# 가장 많이 나온 숫자  n개 찾기
count = Counter(num_list)
most_num=count.most_common(1)

print(most_num)