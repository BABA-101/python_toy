# Flask로 간단한 웹서버 만들기
from flask import Flask

app =Flask(__name__)

#주소로 접속하면 hello 반환.
@app.route('/')
def hello():
    return "hello"

# main함수
def main():
    # flask 웹서버 실행
    app.run(debug=True,port=8888)

#코드 직접 실행 시 main()함수를 실행
# __name__은 코드를 직접 실행 시, 이름이 __name__
# 코드가 모듈로 동작할 시, __name__이 모듈 이름이 되는 것.
# if __name== '__main__'의 의미는 코드를 직접 실행 시 조건이 참이 되는 것이다. cmd실행 의미하는듯
if __name__=="__main__":
    main()