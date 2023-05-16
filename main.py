from flask import Flask
import test

app = Flask(__name__)


@app.route("/")
def home():
    return test


# @app.route("/salvador")
# def salvador():
#     return test

if __name__ == "__main__":
    app.run(debug=True)
