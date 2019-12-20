from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to student records API!" + "created by Ankush Jain"

if __name__ == "__main__":
    app.run(port=8080, use_reloader=True, debug=True)
