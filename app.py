from unicodedata import category

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model/wine_quality_model.pkl')
scaler = joblib.load('model/wine_scaler.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_view.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    prediction = None
    category = None

    if request.method == 'POST':

        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugar = float(request.form['residual_sugar'])
        chlorides = float(request.form['chlorides'])
        free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
        total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
        density = float(request.form['density'])
        pH = float(request.form['pH'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])
        wine_type = int(request.form['wine_type'])

        data = [[
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
            wine_type
        ]]

        # Scaling data
        data_scaled = scaler.transform(data)

        # Prediksi
        prediction = model.predict(data_scaled)[0]

        print("Prediction =", prediction)

        # Kategori kualitas wine
        if prediction >= 8:
            category = "Excellent Quality Wine 🍷🏆"
        elif prediction >= 7:
            category = "High Quality Wine 🍷"
        elif prediction >= 5:
            category = "Medium Quality Wine 🍇"
        else:
            category = "Low Quality Wine ⚠️"

        print("Category =", category)

    return render_template(
        'prediction.html',
        prediction=round(float(prediction), 2) if prediction is not None else None,
        category=category
    )
if __name__ == '__main__':
    app.run(debug=True)
    
