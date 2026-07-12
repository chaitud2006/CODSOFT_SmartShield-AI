from sklearn.naive_bayes import MultinomialNB
import joblib

def train_model(X_train, y_train):
    # This is the "brain" of our project
    model = MultinomialNB()
    # This is where the training happens
    model.fit(X_train, y_train)
    return model

def save_model(model, vectorizer, filepath):
    # Save the "brain" and the "translator" so we can use them later
    joblib.dump(model, filepath + '/spam_model.pkl')
    joblib.dump(vectorizer, filepath + '/tfidf_vectorizer.pkl')
    print("Model saved successfully!")