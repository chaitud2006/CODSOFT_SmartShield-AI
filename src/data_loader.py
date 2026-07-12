import pandas as pd
import os

def load_data(filepath):
    """This function acts like a librarian; it finds and opens your data."""
    if os.path.exists(filepath):
        data = pd.read_csv(filepath, encoding='latin-1')
        print("Success! Data loaded successfully.")
        return data
    else:
        print("Oops! I couldn't find the file. Check the path.")
        return None