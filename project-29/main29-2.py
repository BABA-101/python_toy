import streamlit as st
import datetime

# date_input(레이블, 값)
# 값: 위젯이 처음 렌더링 되었을 때의 초기값을 의미 (날짜)
d = st.date_input("< 날짜 선택 >", datetime.date.today())

st.write('선택한 날짜: ',d)