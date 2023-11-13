from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>This will be the UNIFINITY Website</p>"


if __name__ == "__main__":
    app.run()
