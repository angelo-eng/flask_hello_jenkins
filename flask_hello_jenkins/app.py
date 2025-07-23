from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Jenkins!"

@app.route('/feature/<name>')
def feature(name):
    return f"Feature for {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
