# 다수의 스레드 동작
# 각 스레드가 경쟁적으로 실행하고 종료.
import threading

#name과 value를 입력받아, value만큼 반복
def sum(name,value):
    for i in range(0,value):
        print(f"{name} : {i} \n")

t1=threading.Thread(target=sum, args=(' No.1 Thread ',10))
t2=threading.Thread(target=sum, args=(' No.2 Thread ',10))

t1.start()
t2.start()

print("----- Main Thread -----")
