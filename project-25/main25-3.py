# DB를 읽는 코드
import pandas as pd
import sqlite3

# DB 접속
db_path=r'project-25\coin.db'
con=sqlite3.connect(db_path,isolation_level=None)

#판다스 이용하여 BTC 데이터 읽기
readed_df=pd.read_sql("SELECT * FROM 'BTC'",con,index_col='index')

print(readed_df)