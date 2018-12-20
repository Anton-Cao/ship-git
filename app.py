from flask import Flask, request
import json
import subprocess

app = Flask(__name__)
app.config.from_json("config.json")

def get_repo(content):
    return content["repository"]["name"]

def execute_script(repo):
    try:
        filename = f"./scripts/{repo}.sh"
        subprocess.call(filename, shell=True)
    except Exception as e:
        print(e)

@app.route('/', methods=["POST"])
def handler():
    if request.is_json:
        content = request.get_json()
    else:
        content = json.loads(request.form.get("payload"))
    try:
        repository = get_repo(content)
        execute_script(repository)
        return "success", 200
    except: # repository not found
        err_msg = f"repository {repository} not found"
        print(err_msg)
        return err_msg, 500

if __name__ == "__main__":
    app.run(port=app.config["PORT"])