import folium

# location: 위도,경도 초기화, zoom_start: 지도 배율
map = folium.Map(location=[37,127],zoom_start=7)

# popup: 클릭 시 팝업
marker=folium.Marker([37.341435483, 126.733026596], popup='한국공학대학교', icon=folium.Icon('blue'))

#마커 추가
marker.add_to(map)

map.save(r'project-27\uni_map.html')