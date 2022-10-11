# socket 모듈: 컴퓨터가 연결된 접속정보를 받아올 때 사용
import socket

in_addr = socket.gethostbyname(socket.gethostname())
# gethostbyname(): 도메인정보로 ip, 별칭 등 host에 대한 정보를 구하는 함수
# gethostname(): 호스트 이름을 얻어오거나 설정한다.

print(in_addr)
