from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "HELLO_WORLD"

if __name__ == "__main__":
    app.run(port=9000, use_reloader=True, debug=True)
