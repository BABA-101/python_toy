# 컴퓨터 정보 출력 - 필요한 정보만 출력하기
import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)  # 반올림. current만
print(f"cpu 속도: {cpu_current_ghz}Ghz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어: {cpu_core}개")

memory = psutil.virtual_memory()
memory_total = round(
    memory.total / 1024 ** 3
)  # GB 표현 위해서 1024**3으로 나눈다. round() 디폴트는 0
print(f"메모리: {memory_total}GB")

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=" ")
    # moundpoint:  C:\
    # fstype: 파일시스템 타입
    # end: print() 디폴트는 개행, end 통해 출력 후 마지막 내용 수정.
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024 ** 3)
    print(f"디스크 크기: {disk_total}GB")

net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024 ** 2, 1)
resv = round(net.bytes_recv / 1024 ** 2, 1)
print(f"보내기: {sent}MB, 받기: {resv}MB")
