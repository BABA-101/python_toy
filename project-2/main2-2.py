import socket

# socket의 socket함수: 소켓 객체 생성
# AF_INET: ipv4 주소 패밀리 / SOCK_STREAM: TCP 스트림 통신
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket으로 외부 사이트에 접속하고, 접속된 정보를 바탕으로 ip확인.
# https의 기본 접속 코드 443
in_addr.connect(("www.google.co.kr", 443))
print(type(in_addr.getsockname()))
