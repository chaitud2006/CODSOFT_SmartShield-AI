import pandas as pd
import re

def clean_text(text):
    # 1. Lowercase everything
    text = text.lower()
    
    # 2. Remove special characters and numbers (keep only letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 3. Remove extra spaces
    text = text.strip()
    
    return text

def process_data(df):
    # We apply our cleaning function to the 'text' column
    df['cleaned_text'] = df['text'].apply(clean_text)
    return df