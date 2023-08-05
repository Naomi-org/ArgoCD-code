from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello my Edwin Enoh , it is indeed that hard work pays . our labour will soon pay off!!!'
