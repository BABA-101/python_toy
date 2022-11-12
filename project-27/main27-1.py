import pandas as pd

filePath=r'python-toy\project-27\고등교육기관 하반기 주소록(2020).xlsx'
df_from_excel=pd.read_excel(filePath,engine='openpyxl')

# 다섯번째 위치를 컬럼으로 설정. 데이터의 이름 의미. (엑셀에서 학교명)
df_from_excel.columns=df_from_excel.loc[4].tolist()

# 0~5행 데이터 버리기. 쓸모없음
df_from_excel=df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)
print(df_from_excel['주소'].values)