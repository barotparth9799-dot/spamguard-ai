# SpamGuard AI

## AI-Powered Spam Message and Email Detection

SpamGuard AI is a machine-learning system that detects whether a message is Spam or Not Spam (Ham).

The system supports both SMS and Email analysis and provides:

- Spam or Safe prediction
- Spam probability
- Safe probability
- Explanation of detected indicators
- Detection history
- Dashboard statistics
- IST-based timestamps

## Live Demo

https://spamguard-ai-7lqq9appr9bcmhkzhuereu.streamlit.app/

## GitHub Repository

https://github.com/barotparth9799-dot/spamguard-ai

## System Workflow

User Input
->
SMS or Email Selection
->
Text Preprocessing
->
TF-IDF Feature Extraction
->
Logistic Regression Classifier
->
Spam or Ham Prediction
->
Probability Calculation
->
Explanation Generation
->
History Storage
->
Dashboard Display

## Dataset

The project uses the UCI SMS Spam Collection dataset.

The dataset contains messages labelled as:

- Ham
- Spam

Duplicate messages were removed during preprocessing before model training.

## Text Preprocessing

The preprocessing pipeline performs:

- Lowercase conversion
- URL replacement
- Email address replacement
- Number replacement
- Special-character cleaning
- Whitespace normalization
- Duplicate removal

## Feature Extraction

The system uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text messages into numerical features.

Both unigrams and bigrams are used to capture useful word patterns.

## Machine Learning Model

Two classification models were compared:

| Model | Accuracy |
|---|---:|
| Multinomial Naive Bayes | 97.29% |
| Logistic Regression | 98.45% |

Logistic Regression was selected as the production model because it achieved better overall performance and stronger spam recall.

## Model Evaluation

Test samples: 1034

| Metric | Result |
|---|---:|
| Accuracy | 98.45% |
| Spam Precision | 93.89% |
| Spam Recall | 93.89% |
| Spam F1 Score | 93.89% |

Confusion Matrix:

895  8
8    123

True Negatives: 895
False Positives: 8
False Negatives: 8
True Positives: 123

## Explanation System

The system provides simple reasons for predictions, including:

- Urgency-based wording
- Promotional or prize-related language
- Suspicious links or call-to-action
- Account verification or security-related wording
- Promotional offer language

## SMS and Email Support

Users can select:

- SMS
- Email

The selected message type is stored in detection history.

## Dashboard

The dashboard provides:

- Total messages analyzed
- Spam detections
- Safe detections
- Detection statistics
- Recent detections

## Detection History

SQLite stores:

- Timestamp
- Message type
- Message
- Prediction
- Spam probability
- Safe probability
- Explanation

New timestamps are stored using India Standard Time (IST).

## System Architecture

USER
 |
 v
WEB INTERFACE
 |
 v
SMS / EMAIL INPUT
 |
 v
TEXT PREPROCESSING
 |
 v
TF-IDF
 |
 v
LOGISTIC REGRESSION
 |
 v
PREDICTION
 |
 +----> PROBABILITY
 |
 +----> EXPLANATION
 |
 v
RESULT DISPLAY
 |
 +----> DASHBOARD
 |
 +----> SQLITE HISTORY

## Technology Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- SQLite
- TF-IDF
- Logistic Regression

## Project Structure

spamguard_ai/
|
+-- data/
|   +-- spam.csv
|   +-- processed_spam.csv
|   +-- SMSSpamCollection
|
+-- models/
|   +-- spamguard_model.joblib
|
+-- src/
|   +-- database/history.py
|   +-- explanation/explainer.py
|   +-- prediction/predict.py
|   +-- preprocessing/text_cleaner.py
|   +-- training/train_model.py
|   +-- training/compare_models.py
|   +-- evaluation.py
|
+-- app.py
+-- requirements.txt
+-- README.md
+-- .gitignore

## Running Locally

Activate the virtual environment and run:

streamlit run app.py

## Limitations

- The model is trained primarily on SMS spam patterns.
- Some sophisticated phishing messages may not always be classified correctly.
- The explanation system uses predefined indicators.
- The system does not connect directly to Gmail, Outlook, WhatsApp, or SMS gateways.

## Future Scope

- Larger and more diverse datasets
- Advanced phishing detection
- Better explainability
- Multilingual spam detection
- Continuous model retraining
- More advanced email analysis

## Project Purpose

SpamGuard AI demonstrates a complete AI system design:

Data
->
Preprocessing
->
Feature Extraction
->
Machine Learning
->
Prediction
->
Explanation
->
Database
->
Dashboard
->
Deployment