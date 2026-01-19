from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Your Python app is working on Vercel!'
