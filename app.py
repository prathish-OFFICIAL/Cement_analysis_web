import pickle
from flask import Flask, render_template, request
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle 
app = Flask(__name__)

# loading model
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the HTML form
    cement = float(request.form['cement'])
    blastFurnace = float(request.form['blastFurnace'])
    flyAsh = float(request.form['flyAsh'])
    water = float(request.form['water'])
    superplasticizer = float(request.form['superplasticizer'])
    courseaggregate = float(request.form['courseaggregate'])
    fineaggregate = float(request.form['fineaggregate'])
    age = float(request.form['age'])

    # transform input features
    features = np.array([cement, blastFurnace, flyAsh, water, superplasticizer, courseaggregate, fineaggregate, age]).reshape(1, -1)
    prediction = model.predict(features).reshape(1, -1)

    return f'Prediction: {prediction[0]}'
if __name__ == '__main__':
    app.run(debug=True)
