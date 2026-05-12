import joblib
import pandas as pd

model = joblib.load("models/cybershield_real.pkl")

def predict(packet):
    result = model.predict(packet)
    return "🚨 ATTACK" if result[0] == 1 else "🟢 SAFE"