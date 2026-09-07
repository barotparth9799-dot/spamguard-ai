import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

BASE_DATA_PATH = "data/processed_spam.csv"
AUGMENTED_DATA_PATH = "data/spamguard_augmented.csv"
PRIZE_DATA_PATH = "data/spamguard_prize_augmented.csv"
MODEL_PATH = "models/spamguard_model.joblib"

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

X = df["clean_message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        sublinear_tf=True
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Total dataset rows:", len(df))
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

joblib.dump(model, MODEL_PATH)
print("\nModel saved to:", MODEL_PATH)