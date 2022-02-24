from flask import Flask

app = Flask('__name__')

@app.route('/')
def home():
    return 'Hello my homepage'

if __name__ == '__name__':
    app.run(debug=True)   #코드 자동 적용을 위해 새로고침