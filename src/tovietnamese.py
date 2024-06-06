import os
import pandas as pd
from deep_translator import GoogleTranslator

current_dir = os.path.dirname(os.path.abspath(__file__))
original_data_folder = os.path.join(current_dir, '..', 'originaldata')
data_folder = os.path.join(current_dir, '..', 'data')

os.makedirs(data_folder, exist_ok=True)
chatwords_dict = {
    "AFAIK": "As Far As I Know",
    "AFK": "Away From Keyboard",
    "ASAP": "As Soon As Possible",
    "ATK": "At The Keyboard",
    "ATM": "At The Moment",
    "A3": "Anytime, Anywhere, Anyplace",
    "BAK": "Back At Keyboard",
    "BBL": "Be Back Later",
    "BBS": "Be Back Soon",
    "BFN": "Bye For Now",
    "B4N": "Bye For Now",
    "BRB": "Be Right Back",
    "BRT": "Be Right There",
    "BTW": "By The Way",
    "B4": "Before",
    "B4N": "Bye For Now",
    "CU": "See You",
    "CUL8R": "See You Later",
    "CYA": "See You",
    "FAQ": "Frequently Asked Questions",
    "FC": "Fingers Crossed",
    "FWIW": "For What It's Worth",
    "FYI": "For Your Information",
    "GAL": "Get A Life",
    "GG": "Good Game",
    "GN": "Good Night",
    "GMTA": "Great Minds Think Alike",
    "GR8": "Great!",
    "G9": "Genius",
    "IC": "I See",
    "ICQ": "I Seek you (also a chat program)",
    "ILU": "ILU: I Love You",
    "IMHO": "In My Honest/Humble Opinion",
    "IMO": "In My Opinion",
    "IOW": "In Other Words",
    "IRL": "In Real Life",
    "KISS": "Keep It Simple, Stupid",
    "LDR": "Long Distance Relationship",
    "LMAO": "Laugh My A.. Off",
    "LOL": "Laughing Out Loud",
    "LTNS": "Long Time No See",
    "L8R": "Later",
    "MTE": "My Thoughts Exactly",
    "M8": "Mate",
    "NRN": "No Reply Necessary",
    "OIC": "Oh I See",
    "PITA": "Pain In The A..",
    "PRT": "Party",
    "PRW": "Parents Are Watching",
    "QPSA?": "Que Pasa?",
    "ROFL": "Rolling On The Floor Laughing",
    "ROFLOL": "Rolling On The Floor Laughing Out Loud",
    "ROTFLMAO": "Rolling On The Floor Laughing My A.. Off",
    "SK8": "Skate",
    "STATS": "Your sex and age",
    "ASL": "Age, Sex, Location",
    "THX": "Thank You",
    "TTFN": "Ta-Ta For Now!",
    "TTYL": "Talk To You Later",
    "U": "You",
    "U2": "You Too",
    "U4E": "Yours For Ever",
    "WB": "Welcome Back",
    "WTF": "What The F...",
    "WTG": "Way To Go!",
    "WUF": "Where Are You From?",
    "W8": "Wait...",
    "7K": "Sick:-D Laugher",
    "TFW": "That feeling when",
    "MFW": "My face when",
    "MRW": "My reaction when",
    "IFYP": "I feel your pain",
    "TNTL": "Trying not to laugh",
    "JK": "Just kidding",
    "IDC": "I don't care",
    "ILY": "I love you",
    "IMU": "I miss you",
    "ADIH": "Another day in hell",
    "ZZZ": "Sleeping, bored, tired",
    "WYWH": "Wish you were here",
    "TIME": "Tears in my eyes",
    "BAE": "Before anyone else",
    "FIMH": "Forever in my heart",
    "BSAAW": "Big smile and a wink",
    "BWL": "Bursting with laughter",
    "BFF": "Best friends forever",
    "CSL": "Can't stop laughing"
}
chatwords_dict = {key.lower(): value for key, value in chatwords_dict.items()}

# Function to handle chatwords
def handle_chatwords(text, chatwords_dict):
    words = text.lower().split()
    handled_words = [chatwords_dict.get(word, word) for word in words]
    return ' '.join(handled_words)

# Function to translate English to Vietnamese
def translate_to_vietnamese(text):
    try:
        translated_text = GoogleTranslator(source='en', target='vi').translate(text)
        return translated_text
    except Exception as e:
        print(f"Error translating text: {text}, error: {e}")
        return text

# Processing data
def process_file(input_file, output_file, chatwords_dict):
    data = []
    try:
        with open(input_file, 'r', encoding='latin1') as infile:
            for line in infile:
                parts = line.strip().split(';')
                if len(parts) != 2:
                    print(f"Line skipped (incorrect format): {line}")
                    continue
                text, label = parts
                print(f"Original text: {text}, Label: {label}")
                text = handle_chatwords(text, chatwords_dict)
                print(f"Text after handling chatwords: {text}")
                translated_text = translate_to_vietnamese(text)
                print(f"Translated text: {translated_text}")
                data.append([translated_text, label])
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")
    
    df = pd.DataFrame(data, columns=['text', 'label'])
    df.to_excel(output_file, index=False)

files = ['train.txt','test.txt','val.txt']

for file in files:
    input_path = os.path.join(original_data_folder, file)
    output_path = os.path.join(data_folder, file.replace('.txt', '.xlsx'))
    print(f"Processing file: {input_path}")
    process_file(input_path, output_path, chatwords_dict)

print("done")
