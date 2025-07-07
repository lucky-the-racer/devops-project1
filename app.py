
from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "i am lucky nangal aala"

@app.route("/phone")
def lwphone():
	return "8233727217"

app.run(host="0.0.0.0")
