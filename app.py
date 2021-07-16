from flask import Flask,render_template,request
import numpy as np  
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score 
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/predict",methods=["POST"])

def predict():

    if request.method == "POST":
    
        year = request.form["year"]
        Month = request.form["month"]
        
        data=[[int(year),int(Month)]]
        tmpt=pickle.load(open('./model/weather.pkl','rb'))
        prediction=tmpt.predict(data)[0]
    return render_template("index.html",prediction=prediction)
    
    
if __name__ == '__main__':  
    app.run(debug = True)  