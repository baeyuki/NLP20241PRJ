from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd
from dataprep.dataprocessing import clean_text

app = Flask(__name__)

# Load trained model
model = load_model('src/bilstm_model.h5')

# Load label encoder
label_encoder = np.load('src/label_encoder.npy', allow_pickle=True).item()

# Load tokenizer
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(pd.read_csv('data/train.txt', delimiter=';', header=None)[0])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sentence = request.form['sentence']
        cleaned_sentence = clean_text(sentence)
        tokenized_sentence = tokenizer.texts_to_sequences([cleaned_sentence])
        padded_sentence = pad_sequences(tokenized_sentence, maxlen=100, padding='post')
        prediction = model.predict(padded_sentence)
        predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])[0]
        return render_template('result.html', sentence=sentence, prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
