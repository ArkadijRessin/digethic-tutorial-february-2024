from flask import Flask, Response, request
from flask_cors import CORS
import os
import pandas as pd
import pickle
app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET"])
def index():
    return {"hello": "world"}
