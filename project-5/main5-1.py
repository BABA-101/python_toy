# 컴퓨터의 정보를 확인할 때 사용하는 라이브러리
import psutil

# CPU 속도
cpu = psutil.cpu_freq()
print(cpu)

# 물리 코어 수
# psutil.cpu_count()는 logical=true 디폴트 (논리적cpu)
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

# 메모리 정보
memory = psutil.virtual_memory()
print(memory)

# 디스크 정보
disk = psutil.disk_partitions()
print(disk)

# 네트워크 정보
net = psutil.net_io_counters()
print(net)
