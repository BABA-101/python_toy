# 정규식 이용하여 이메일 형식을 추출
# 정규표현식 라이브러리 re
import re

test_string = """
aaa@bbb.com
abc@abc.com
123@ok.co.kr
tqwdas@test.com
user111@test.com
amamama@123.com
qwewqw@1234
no.co.kr
no.kr
"""

results= re.findall(r'[\w\.-]+@[\w\.-]+',test_string)
print(results)
