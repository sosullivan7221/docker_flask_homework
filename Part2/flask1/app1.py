from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the first part of my app. The second app will add two numbers'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')