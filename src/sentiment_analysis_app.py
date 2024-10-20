import re
import pickle
import streamlit as st
import os

# Title of the Streamlit app
st.title("Sentiment Analysis I2@FSS")

# Load the vectorizer and model from the models directory
# Use os.path.join to construct the path
current_dir = os.path.dirname(__file__)
models_dir = os.path.join(current_dir, '../models')
vect = pickle.load(open(os.path.join(models_dir, "vect.pickle"), "rb"))
model = pickle.load(open(os.path.join(models_dir, "model.pickle"), "rb"))

# Input box for user comment
text = st.text_input("Leave your comment")

if text:  # Check if the input is not empty
    # Preprocess the input text
    tmp = re.sub(r'[^a-zA-Z]', '', str(text))  # Remove all special characters and punctuation
    tmp = re.sub(r'\s+', ' ', tmp)  # Remove multiple white spaces
    tmp = re.sub(r'\s+[a-zA-Z]\s+', ' ', tmp)  # Remove single characters
    tmp = tmp.lower()  # Lowercasing

    # Transform the input using the vectorizer
    X = vect.transform([tmp]).toarray()

    # Make prediction
    pred = model.predict(X)

    # Display prediction when button is pressed
    if st.button("Predict"):
        st.success(pred[0])  # Display the first prediction
