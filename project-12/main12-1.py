# 판다스를 통해서 정보를 엑셀로 저장하는 코드
import pandas as pd

df = pd.DataFrame([
    ["홍길동", "1990.01.01", "2021-0001"],
    ["황기둥", "1995.05.18", "2021-0002"],
    ["김진기", "1996.03.27", "2021-0003"],
    ["한명기", "2010.12.30", "2021-0004"],
    ["김도토리", "2012.07.14", "2021-0005"],
    ["이철수", "2009.08.26", "2021-0006"]
])

print(df)
#데이터프레임을 엑셀로 저장, 인덱스와 헤더는 저장하지 않는다 (0 1 2 이런것들)
df.to_excel(r'project-12\수료증명단생성.xlsx', index=False, header=False)

