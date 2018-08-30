from flask import Flask

app = Flask(__name__) # __name__ means the current file

@app.route("/") # "/" means the default webpage
def index():
    return "Hello, world!!!"
