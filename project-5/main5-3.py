# 1초마다 반복하는 컴퓨터 정보 출력
import psutil

curr_sent = 0
curr_resv = 0

prev_sent = 0
prev_recv = 0

while True:
    # cpu 사용량을 1초동안의 평균값으로 구함
    cpu_p = psutil.cpu_percent(interval=1)
    print(f"CPU 사용량: {cpu_p}%")

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024 ** 3, 1)
    print(f"사용 가능한 메모리: {memory_avail}GB")

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent / 1024 ** 2
    curr_recv = net.bytes_recv / 1024 ** 2

    # 현재 측정 값에서 이전에 측정한 값을 빼면 1초동안 보내는 데이터를 구할 수 있다.
    sent = round(curr_sent - prev_sent, 1)
    recv = round(curr_recv - prev_recv, 1)

    print(f"보내기: {sent}MB, 받기: {recv}MB")
    print("--------------------------------------------------------")

    prev_sent = curr_sent
    prev_recv = curr_recv
