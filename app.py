from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    longitude = float(request.form['longitude'])
    latitude = float(request.form['latitude'])
    housing_median_age = float(request.form['housing_median_age'])
    total_rooms = float(request.form['total_rooms'])
    total_bedrooms = float(request.form['total_bedrooms'])
    population = float(request.form['population'])
    households = float(request.form['households'])
    median_income = float(request.form['median_income'])
    ocean_proximity = request.form['ocean_proximity']

    data = {
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    }

    import pandas as pd
    input_df = pd.DataFrame(data)

    prediction = model.predict(input_df)[0]
    return render_template(
        'index.html',
        prediction_text=f'Estimated House Price: ${prediction:,.2f}'
    )

if __name__ == '__main__':
    app.run(debug=True)