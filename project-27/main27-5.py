import pandas as pd
import folium

path=r'project-27\univ_address.xlsx'
df_from_excel=pd.read_excel(path,engine='openpyxl',header=None)

df_from_excel.columns=['학교이름','주소','x','y']

name_list=df_from_excel['학교이름'].to_list()
addr_list=df_from_excel['주소'].to_list()
position_x_list=df_from_excel['x'].to_list()
position_y_list=df_from_excel['y'].to_list()

# 기본 맵 설정, location=[위도,경도]
map=folium.Map(location=[37,127],zoom_start=7)

for i in range(len(name_list)):
    # x값이 0이 아닐 때 
    if position_x_list[i] != 0:
        # Marker([위도,경도],popup, icon)
        marker=folium.Marker([position_y_list[i],position_x_list[i]],popup=name_list[i],icon=folium.Icon('blue'))
        marker.add_to(map) #마커추가

map.save(r'project-27\uni_map2.html')