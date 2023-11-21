from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    math = 4 + 4
    finalstring = f'Here is the sum of 4 + 4: {math}'
    return finalstring

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')