from flask import Flask

app = Flask("__init__")

@app.route('/')
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)