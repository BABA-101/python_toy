from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/1')
def test1page():
    return "1 page OK"

@app.route('/2')
def test2page():
    return "2 page OK"

def main():
    app.run(debug=True,port=8888)

if __name__ == '__main__':
    main()