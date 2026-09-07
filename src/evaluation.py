import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

MODEL_PATH = "models/spamguard_model.joblib"
BASE_DATA_PATH = "data/processed_spam.csv"
AUGMENTED_DATA_PATH = "data/spamguard_augmented.csv"
PRIZE_DATA_PATH = "data/spamguard_prize_augmented.csv"

model = joblib.load(MODEL_PATH)

base_df = pd.read_csv(BASE_DATA_PATH)
augmented_df = pd.read_csv(AUGMENTED_DATA_PATH)
prize_df = pd.read_csv(PRIZE_DATA_PATH)

base_data = base_df[["label", "clean_message"]]

augmented_data = augmented_df[["label", "message"]].copy()
augmented_data["clean_message"] = augmented_data["message"].astype(str).str.lower()
augmented_data = augmented_data[["label", "clean_message"]]

prize_data = prize_df[["label", "message"]].copy()
prize_data["clean_message"] = prize_data["message"].astype(str).str.lower()
prize_data = prize_data[["label", "clean_message"]]

df = pd.concat(
    [base_data, augmented_data, prize_data],
    ignore_index=True
)

X_train, X_test, y_train, y_test = train_test_split(
    df["clean_message"],
    df["label"],
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

print("=== SPAMGUARD AI MODEL EVALUATION ===")
print("Total dataset samples:", len(df))
print("Test samples:", len(y_test))
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("Spam Precision:", round(precision_score(y_test, y_pred, pos_label="spam"), 4))
print("Spam Recall:", round(recall_score(y_test, y_pred, pos_label="spam"), 4))
print("Spam F1 Score:", round(f1_score(y_test, y_pred, pos_label="spam"), 4))

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("True Negatives:", cm[0, 0])
print("False Positives:", cm[0, 1])
print("False Negatives:", cm[1, 0])
print("True Positives:", cm[1, 1])