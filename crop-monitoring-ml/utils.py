import random

def generate_soil_moisture_data(temp, humidity, soil_type):
    base = (temp * 0.3) + (humidity * 0.5) + (soil_type * 10)
    moisture = 100 - min(base, 100)
    return round(moisture / 100, 2)

def generate_yield_data(temp, humidity, rainfall, fertilizer):
    yield_estimate = (rainfall * 0.3 + fertilizer * 0.4 + humidity * 0.2 + temp * 0.1)
    return round(yield_estimate, 2)

def generate_climate_data(temp, humidity, month):
    rainfall = random.uniform(0, 300) * (humidity / 100) * (month / 12)
    return round(rainfall, 2)
