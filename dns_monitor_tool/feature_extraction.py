# feature_extraction.py
import pandas as pd

def extract_features(file):
    df = pd.read_csv(file)
    
    # Use 'Query' column instead of 'domain' to match CSV structure
    # Also clean the domain names (remove trailing dots)
    df['clean_query'] = df['Query'].str.rstrip('.')
    
    # Extract features from the cleaned query/domain names
    df['domain_length'] = df['clean_query'].apply(len)
    df['num_dots'] = df['clean_query'].apply(lambda x: x.count('.'))
    df['has_numbers'] = df['clean_query'].apply(lambda x: any(char.isdigit() for char in x))
    df['has_hyphen'] = df['clean_query'].apply(lambda x: '-' in x)
    df['subdomain_count'] = df['clean_query'].apply(lambda x: len(x.split('.')) - 2 if len(x.split('.')) > 2 else 0)
    
    # Additional suspicious patterns
    df['is_suspicious_length'] = df['domain_length'] > 50  # Very long domain names
    df['has_suspicious_chars'] = df['clean_query'].apply(lambda x: any(c in x for c in ['_', '%', '@']))
    
    return df[['domain_length', 'num_dots', 'has_numbers', 'has_hyphen', 'subdomain_count', 'is_suspicious_length', 'has_suspicious_chars']]
