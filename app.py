from flask import Flask, request

app = Flask(__name__)
app.config.from_json("config.json")

@app.route('/', methods=["POST"])
def handler():
    pass

if __name__ == "__main__":
    app.run(port=app.config["PORT"])