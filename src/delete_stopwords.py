import pandas as pd
import re
import string

def load_stopwords(stopwords_file):
    with open(stopwords_file, 'r', encoding="utf8", errors='ignore') as file:
        stopwords = file.read().splitlines()
    return set(stopwords)

def clean_text(text, stopwords):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub("\s+", " ", text)
    text = " ".join([word for word in text.split() if word not in stopwords])
    return text 

def delete_stopwords(df, stopwords_file):
    stopwords = load_stopwords(stopwords_file)
    df['text'] = df['text'].apply(lambda x: clean_text(x, stopwords))
    return df
