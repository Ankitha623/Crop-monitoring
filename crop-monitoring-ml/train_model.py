import joblib
from sklearn.linear_model import LinearRegression
from utils import generate_soil_data, generate_yield_data, generate_climate_data

def train_soil_model():
    df = generate_soil_data()
    X = df[['temperature', 'humidity', 'soil_type']]
    y = df['moisture']
    model = LinearRegression().fit(X, y)
    joblib.dump(model, 'models/soil_model.pkl')

def train_yield_model():
    df = generate_yield_data()
    X = df[['rainfall', 'temperature', 'fertilizer']]
    y = df['yield']
    model = LinearRegression().fit(X, y)
    joblib.dump(model, 'models/yield_model.pkl')

def train_climate_model():
    df = generate_climate_data()
    X = df[['month', 'humidity', 'temperature']]
    y = df['rain_chance']
    model = LinearRegression().fit(X, y)
    joblib.dump(model, 'models/climate_model.pkl')

if __name__ == "__main__":
    train_soil_model()
    train_yield_model()
    train_climate_model()
    print("✅ All models trained and saved to 'models/' folder.")
