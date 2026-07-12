import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.feature_engineering import create_vectorizer

# A small list of messages
messages = [
    "free money win prize",
    "hello how are you",
    "win big money now"
]

# Turn words into numbers!
vectorizer = create_vectorizer(messages)
vectors = vectorizer.transform(messages)

print("Words the computer learned:")
print(vectorizer.get_feature_names_out())
print("\nLook at the numbers (this is how the computer sees the words):")
print(vectors.toarray())