# 사전 준비물: 로또 당첨번호 자료 xls파일
import pandas as pd
file_path=r'project-26\lotto.xlsx'
# openpyxl 엔진을 사용하여 판다스 데이터프레임으로 엑셀 파일 불러오기
df_from_excel=pd.read_excel(file_path,engine='openpyxl')

# index[0,1]번째 줄을 삭제
df_from_excel=df_from_excel.drop(index=[0,1])

# 컬럼이름 재정의
df_from_excel.columns=[
    '년도','회차','추첨일','1등당첨자수',
    '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
    '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
    '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
    '당첨번호4','당첨번호5','당첨번호6','보너스번호'
]

#앞부분 데이터만 출력
print(df_from_excel.head())
print(df_from_excel['회차'].values)
print(df_from_excel['1등당첨금액'].values)