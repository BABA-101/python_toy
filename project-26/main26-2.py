# 회차별 당첨금액을 그래프로 그려보기
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

file_path=r'project-26\lottol.xls'
df_from_excel=pd.read_excel(file_path,engine='openpyxl')

df_from_excel=df_from_excel.drop(index=[0,1])

df_from_excel.columns=[
    '년도','회차','추첨일','1등당첨자수',
    '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
    '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
    '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
    '당첨번호4','당첨번호5','당첨번호6','보너스번호'
]

# 엑셀 파일 확인해보면, 당첨금액이 숫자+,+원 형태로 되어있음. ,와 원 제거
df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-|가-힣],+',repl=r' ', regex=True)
df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-|가-힣],+',repl=r' ', regex=True)
df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-|가-힣],+',repl=r' ', regex=True)
df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-|가-힣],+',repl=r' ', regex=True)
df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-|가-힣],+',repl=r' ', regex=True)

# 값을 숫자형태로 다시 데이터프레임에 저장.
df_from_excel['1등당첨금액']=pd.to_numeric(df_from_excel['1등당첨금액'])
df_from_excel['2등당첨금액']=pd.to_numeric(df_from_excel['2등당첨금액'])
df_from_excel['3등당첨금액']=pd.to_numeric(df_from_excel['3등당첨금액'])
df_from_excel['4등당첨금액']=pd.to_numeric(df_from_excel['4등당첨금액'])
df_from_excel['5등당첨금액']=pd.to_numeric(df_from_excel['5등당첨금액'])

print(df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']])

# 그래프 이름 표시할 때 한글을 사용하기 위한 폰트 설정
font_path='C:\windows\Fonts\NGULIM.TTF'
font=font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font)

# 회차의 마지막 100개 데이터만 x축으로 사용
x=df_from_excel['회차'].iloc[:100].values
# 당첨금액의 마지막 100개의 데이터만 y축으로 사용. 단위 억원 표시 위해 /1억
price=df_from_excel['1등당첨금액'].iloc[:100].values / 100000000

# 그래프의 초기 표시 크기 결정
plt.figure(figsize=(10.6))
plt.xlabel('회차')
plt.ylabel('당첨금액(단위:억원')

#바의 x,y값 폭 지정하여 그래프 그리기
plt.bar(x,price,width=0.4)
plt.show()