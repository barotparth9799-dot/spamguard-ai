import joblib
import sys
from pathlib import Path
from src.explanation.explainer import explain_message

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "spamguard_model.joblib"
model = joblib.load(MODEL_PATH)

def predict_message(message):
    message = str(message)
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)
    spam_probability = float(probabilities[classes.index("spam")])
    ham_probability = float(probabilities[classes.index("ham")])
    explanation = explain_message(message, prediction)
    return {"prediction": prediction, "spam_probability": spam_probability, "safe_probability": ham_probability, "explanation": explanation}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a message to analyze.")
        sys.exit(1)
    result = predict_message(sys.argv[1])
    print("Prediction:", result["prediction"])
    print("Spam probability:", round(result["spam_probability"], 4))
    print("Safe probability:", round(result["safe_probability"], 4))
    print("Explanation:")
    for reason in result["explanation"]:
        print("-", reason)
