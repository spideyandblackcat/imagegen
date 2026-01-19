from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    # PASTE YOUR ONE-FILE CODE LOGIC HERE
    return "Your app is running!"
  
