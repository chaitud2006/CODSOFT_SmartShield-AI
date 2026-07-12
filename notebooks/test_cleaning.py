import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text
import pandas as pd
from src.preprocessing import clean_text

# Let's test one message
sample_message = "FREE entry in 2 a wkly comp to win FA Cup final tkts!!!"
cleaned = clean_text(sample_message)

print(f"Original: {sample_message}")
print(f"Cleaned:  {cleaned}")