# SpamGuard AI

## AI-Powered Spam Message and Email Detection

SpamGuard AI is a machine-learning based system that detects whether a text message or email is **Spam** or **Not Spam (Ham)**.

The system combines text preprocessing, TF-IDF feature extraction, Logistic Regression classification, explanation generation, SQLite history storage, and a Streamlit web interface into one complete AI application.

---

## Live Demo

https://spamguard-ai-7lqq9appr9bcmhkzhuereu.streamlit.app/

## GitHub Repository

https://github.com/barotparth9799-dot/spamguard-ai

---

## Project Objective

The main objective of SpamGuard AI is to provide an easy-to-use system for identifying potentially unwanted or fraudulent messages.

The system accepts SMS or email text and provides:

- Spam or Not Spam prediction
- Spam probability
- Safe probability
- Explanation of detected spam indicators
- Detection history
- Dashboard statistics
- SMS and Email classification

---

## System Workflow

The complete workflow of SpamGuard AI is:

User Input
→ Message Type Selection
→ Text Preprocessing
→ TF-IDF Feature Extraction
→ Logistic Regression Classifier
→ Prediction and Probability
→ Explanation Generation
→ SQLite History
→ Dashboard and Results

---

## System Architecture

The system follows this architecture:

USER

↓

SPAMGUARD AI WEB INTERFACE

↓

INPUT PROCESSING
(SMS / EMAIL)

↓

TEXT PREPROCESSING
(Lowercase, Cleaning, Token Handling)

↓

TF-IDF FEATURE EXTRACTION

↓

LOGISTIC REGRESSION CLASSIFIER

↓

RESULT PROCESSOR

↓

Prediction + Probability + Explanation

↓

RESULT DISPLAY + SQLITE HISTORY

↓

DASHBOARD / HISTORY

---

## Dataset

The primary dataset used for this project is the **UCI SMS Spam Collection**.

The dataset contains labelled SMS messages classified as:

- ham
- spam

The original dataset contained 5,574 messages.

After data cleaning and duplicate removal, the processed dataset contains 5,169 unique messages.

Class distribution in the processed dataset:

- Ham: 4,516
- Spam: 653

Additional targeted augmentation data was added to improve generalization for Indian-style cash, prize, reward, and promotional spam messages.

The final training data contains:

- Original processed samples: 5,169
- Targeted augmentation samples: 50
- Final combined dataset: 5,219 samples

---

## Data Preprocessing

The preprocessing stage prepares raw messages for machine-learning classification.

The system performs operations such as:

- Converting text to lowercase
- Removing unnecessary characters
- Handling URLs
- Handling email addresses
- Handling numerical values
- Removing excessive whitespace
- Removing duplicate messages

Examples of special patterns are represented using tokens such as:

- URLTOKEN
- EMAILTOKEN
- NUMTOKEN

This helps the model focus on useful text patterns instead of individual variable values.

---

## Feature Extraction

SpamGuard AI uses **TF-IDF (Term Frequency-Inverse Document Frequency)** for feature extraction.

The TF-IDF vectorizer uses:

- Unigrams
- Bigrams
- Minimum document frequency of 2
- Sublinear TF scaling

This converts the processed text into numerical feature vectors that can be used by the machine-learning classifier.

---

## Machine Learning Model

The production model used by SpamGuard AI is **Logistic Regression**.

The classifier uses:

- Maximum iterations: 1000
- Balanced class weights

Logistic Regression was selected after comparing different approaches because it provided strong classification performance while remaining simple, fast, and suitable for a lightweight system.

---

## Model Comparison

Two machine-learning approaches were evaluated during development:

### Multinomial Naive Bayes

Initial evaluation:

- Accuracy: 97.29%
- Spam Precision: 100.00%
- Spam Recall: 78.63%
- Spam F1 Score: 88.03%

### Logistic Regression

The Logistic Regression approach produced better overall spam detection performance and was therefore selected as the production model.

---

## Final Model Evaluation

The final SpamGuard AI model uses TF-IDF feature extraction with Logistic Regression and includes targeted spam augmentation data.

Final evaluation results:

- Total dataset samples: 5,219
- Test samples: 1,044
- Accuracy: 98.47%
- Spam Precision: 93.62%
- Spam Recall: 94.96%
- Spam F1 Score: 94.29%

### Confusion Matrix

```text
[[896   9]
 [  7 132]]Deployment refresh - latest production model verified locally.
