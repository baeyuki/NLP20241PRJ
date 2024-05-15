import pandas as pd
import re
import string
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            text, label = line.strip().split(';')  
            data.append({'text': text, 'label': label})
    return pd.DataFrame(data)

def load_datasets():
    train_df = read_data('../data/train.txt')
    test_df = read_data('../data/test.txt')
    val_df = read_data('../data/val.txt')
    return train_df, test_df, val_df

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub("\s+", " ", text)
    text = " ".join([word for word in text.split() if word not in STOPWORDS])
    return text 

def preprocess_data(df):
    df['text'] = df["text"].apply(clean_text)
    return df

def prepare_datasets():
    train_df, test_df, val_df = load_datasets()
    train_df = preprocess_data(train_df)
    test_df = preprocess_data(test_df)
    val_df = preprocess_data(val_df)
    return train_df, test_df, val_df
