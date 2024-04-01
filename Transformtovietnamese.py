import pandas as pd
from googletrans import Translator, LANGUAGES

translator = Translator()

df = pd.read_csv('text1.csv')

def translate_to_vietnamese(text):
    try:
        translated_text =translator.translate(text, src='en',dest ='vi').text
        return translated_text
    except Exception as e:
        print(f"error : {e}")
        return text
    
    
df["text in vietnamese"]= df["text"].apply(translate_to_vietnamese)

new_df=df[["text in vietnamese","label"]]

new_df.to_csv("data.csv", index=False)
print('done')
    