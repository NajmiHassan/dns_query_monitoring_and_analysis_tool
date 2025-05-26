# feature_extraction.py
import pandas as pd

def extract_features(file):
    df = pd.read_csv(file)
    df['domain_length'] = df['domain'].apply(len)
    df['num_dots'] = df['domain'].apply(lambda x: x.count('.'))
    df['has_numbers'] = df['domain'].apply(lambda x: any(char.isdigit() for char in x))
    return df[['domain_length', 'num_dots', 'has_numbers']]
