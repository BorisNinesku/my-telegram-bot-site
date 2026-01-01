from flask import Flask
import os

app = Flask(__name__)

@app.route('')
def index():
    return 'h1Привет, это мой сайт!h1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
