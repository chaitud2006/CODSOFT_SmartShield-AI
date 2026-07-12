import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text
from src.feature_engineering import create_vectorizer
from src.train import train_model, save_model

# 1. Our Training Data
texts = ["free money win", "hello dear", "win big prize", "meeting at home"]
labels = ["spam", "ham", "spam", "ham"] # 0 for ham, 1 for spam (we'll map them)

# 2. Prepare Labels (0 and 1)
label_map = {"ham": 0, "spam": 1}
y = [label_map[l] for l in labels]

# 3. Clean and Vectorize
cleaned_texts = [clean_text(t) for t in texts]
vectorizer = create_vectorizer(cleaned_texts)
X = vectorizer.transform(cleaned_texts)

# 4. Train!
model = train_model(X, y)

# 5. Save the Brain
save_model(model, vectorizer, 'models')

print("Training complete! Your AI is now smart enough to guess.")