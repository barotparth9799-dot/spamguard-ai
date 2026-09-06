import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv("data/processed_spam.csv")
X_train, X_test, y_train, y_test = train_test_split(df["clean_message"], df["label"], test_size=0.20, random_state=42, stratify=df["label"])

models = {
    "Multinomial Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced")
}

for name, classifier in models.items():
    model = Pipeline([( "tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=2, sublinear_tf=True)), ("classifier", classifier)])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("\\n===", name, "===")
    print("Accuracy:", round(accuracy_score(y_test, pred), 4))
    print("Spam Precision:", round(precision_score(y_test, pred, pos_label="spam"), 4))
    print("Spam Recall:", round(recall_score(y_test, pred, pos_label="spam"), 4))
    print("Spam F1:", round(f1_score(y_test, pred, pos_label="spam"), 4))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))
