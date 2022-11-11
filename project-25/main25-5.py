# 얻은 데이터 DB에 저장
import pandas as pd
import sqlite3

db_path=r"project25\coin.db"
con=sqlite3.connect(db_path,isolation_level=None)

# BTC에서 중복된 값 제외하고 불러옴
readed_df=pd.read_sql("SELECT DISTINCT * FROM 'BTC",con,index_col='index')
# BTC-NEW라는 이름으로 저장
readed_df.to_sql('BTC_NEW',con,if_exists='replace')

print(readed_df)