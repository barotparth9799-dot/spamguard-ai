import re
import pandas as pd


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+', ' URLTOKEN ', text)
    text = re.sub(r'www\.\S+', ' URLTOKEN ', text)
    text = re.sub(r'\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b', ' EMAILTOKEN ', text)
    text = re.sub(r'\d+', ' NUMTOKEN ', text)
    text = re.sub(r'[^a-zA-Z_ ]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def prepare_dataset(input_path='data/spam.csv', output_path='data/processed_spam.csv'):
    df = pd.read_csv(input_path, encoding='utf-8')
    df = df.drop_duplicates(subset=['message']).reset_index(drop=True)
    df['clean_message'] = df['message'].apply(clean_text)
    df.to_csv(output_path, index=False, encoding='utf-8')
    return df


if __name__ == '__main__':
    df = prepare_dataset()
    print('Processed rows:', len(df))
    print('Labels:')
    print(df['label'].value_counts())
