import pandas as pd
from flask import Flask
from flask_ngrok import run_with_ngrok
from flask import jsonify

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def converte():
    excell = pd.read_excel('dados.xlsx', sheet_name='person')
    json_str = excell.to_json(orient='records')
    return jsonify(json_str).json


if __name__ == "__main__":
    app.run()




