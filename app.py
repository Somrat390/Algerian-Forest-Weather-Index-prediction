from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#import ridge regressor and standard scaler pickle files
ridge_model = pickle.load(open("Model/ridge.pkl", "rb")) 
scaler = pickle.load(open("Model/scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = int(request.form.get('Classes'))
        region = request.form.get('region')

        new_data_scaled = scaler.transform(np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, region]]))

        prediction = ridge_model.predict(new_data_scaled)

        return render_template('home.html', prediction=prediction)

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')