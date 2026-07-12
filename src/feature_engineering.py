from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer(text_data):
    # This tool counts the words and gives them a "weight"
    vectorizer = TfidfVectorizer(stop_words='english')
    # We "fit" it on the text to learn the words
    vectorizer.fit(text_data)
    return vectorizer