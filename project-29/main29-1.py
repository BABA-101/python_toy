#  flask 대신 쓸만한 웹앱 라이브러리
# streamlit run main29-1.py
import streamlit as st

data_list = {1,2,3,4,5,6,7,8,9,10}
st.write('''
         My site!!!!!!!!!
         ''')

# 차트 그리기
st.line_chart(data_list)
