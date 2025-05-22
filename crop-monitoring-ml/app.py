from utils import generate_soil_moisture_data, generate_yield_data, generate_climate_data
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for soil moisture prediction
@app.route('/soil', methods=['GET', 'POST'])
def soil_moisture():
    if request.method == 'POST':
        # Get the data from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        soil_type = int(request.form['soil_type'])

        # Generate synthetic soil moisture data
        moisture = generate_soil_moisture(temperature, humidity, soil_type)
        return render_template('soil_moisture.html', moisture=moisture)

    return render_template('soil_moisture.html')

# Route for yield prediction
@app.route('/yield', methods=['GET', 'POST'])
def yield_prediction():
    if request.method == 'POST':
        # Get the data from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        fertilizer = float(request.form['fertilizer'])

        # Generate synthetic yield prediction data
        yield_prediction = generate_yield_prediction(temperature, humidity, rainfall, fertilizer)
        return render_template('yield_prediction.html', yield_prediction=yield_prediction)

    return render_template('yield_prediction.html')

# Route for climate prediction
@app.route('/climate', methods=['GET', 'POST'])
def climate_prediction():
    if request.method == 'POST':
        # Get the data from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        month = int(request.form['month'])

        # Generate synthetic rainfall data based on inputs
        rainfall = generate_climate_data(temperature, humidity, month)
        return render_template('climate_prediction.html', rainfall=rainfall)

    return render_template('climate_prediction.html')

# Function to generate synthetic soil moisture data
def generate_soil_moisture(temperature, humidity, soil_type):
    moisture = random.uniform(10, 50) * (humidity / 100) * (soil_type / 2)
    return round(moisture, 2)

# Function to generate synthetic yield prediction
def generate_yield_prediction(temperature, humidity, rainfall, fertilizer):
    yield_prediction = random.uniform(0, 1000) * (temperature / 30) * (humidity / 100) * (rainfall / 200) * (fertilizer / 50)
    return round(yield_prediction, 2)

# Function to generate synthetic climate data (rainfall)
def generate_climate_data(temperature, humidity, month):
    rainfall = random.uniform(0, 300) * (humidity / 100) * (month / 12)
    return round(rainfall, 2)

if __name__ == "__main__":
    app.run(debug=True)
