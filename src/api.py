from flask import Flask, Response, request
from flask_cors import CORS
import os
import pandas as pd
import pickle

app = Flask(__name__)

CORS(app)

training_data = pd.read_csv(os.path.join('data', 'auto-mpg-training-data.csv') )
file_to_open = open (os.path.join('data', 'models', 'baummethoden_lr.pickle'), 'rb')

trained_model = pickle.load(file_to_open)
file_to_open.close()

# print(training_data)

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/predict", methods=["GET"])
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    if (zylinder and ps and gewicht and beschleunigung and baujahr):
        prediction = trained_model.predict([[zylinder, ps, gewicht, beschleunigung, baujahr]])
        print(prediction)
        return {"result": prediction[0]}

    return Response ('Please provide all neccessary parameters to get a prediction: zylinder and ps and gewicht and beschleunigung and baujahr',  mimetype="application/json")

# http://127.0.0.1:5000/predict?zylinder=6&ps=133&gewicht=3410&beschleunigung=15.8&baujahr=78
