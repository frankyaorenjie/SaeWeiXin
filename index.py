from bottle import Bottle, run

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle1"