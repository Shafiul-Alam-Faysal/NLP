import os
import joblib
from src.features import query_point_creator

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

model = joblib.load(MODEL_PATH)

def predict_duplicate(q1, q2):
    features = query_point_creator(q1, q2)

    prediction = model.predict(features)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(features)[0]

    return prediction, probability