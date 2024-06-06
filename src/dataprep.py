import pandas as pd
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        return result['encoding']

def read_data(file_path):
    encoding = detect_encoding(file_path)
    data = pd.read_excel(file_path)
    return data

def load_datasets():
    train_file = 'C:/Users/thanh/Documents/NLP20241PRJ-1/data/train.xlsx'
    test_file = 'C:/Users/thanh/Documents/NLP20241PRJ-1/data/test.xlsx'
    val_file = 'C:/Users/thanh/Documents/NLP20241PRJ-1/data/val.xlsx'
    
    train_df = read_data(train_file)
    test_df = read_data(test_file)
    val_df = read_data(val_file)
    
    return train_df, test_df, val_df

if __name__ == "__main__":
    train_df, test_df, val_df = load_datasets()
    print(train_df.head())
    print(test_df.head())
    print(val_df.head())
