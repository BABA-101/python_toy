import re

test_string = """
abc@abc.com
123@ok.co.kr
user111@test.com
user111@test.com
user111@test.com
qwewqw@1234
no.co.kr
no.kr
"""

results=re.findall(r'[\w\.-]+@[\w\.-]+',test_string)
results=list(set(results))  # set 사용하여 중복을 제거

print(results)