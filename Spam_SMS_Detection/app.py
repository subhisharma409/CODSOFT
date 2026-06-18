import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import string
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
ps = PorterStemmer()

from nltk.corpus import stopwords
import string
import re

stop_words = set(stopwords.words('english'))
stop_words.discard('won')
stop_words.discard('not')
stop_words.discard('no')

def transform_text(text):
    text=text.lower()
    # Replace URLs
    text = re.sub(r'http\S+|www\S+', ' URL ', text)

     # Replace email addresses
    text = re.sub(r'\S+@\S+', ' EMAIL ', text)

    # Replace currency symbols
    text = re.sub(r'[$₹£]', ' MONEY ', text)

    # Tokenization
    text=nltk.word_tokenize(text)
    y=[]
    
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

import os

BASE_DIR = os.path.dirname(__file__)

tfidf = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))
model = pickle.load(open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'rb'))

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter the SMS message")

if st.button("Predict"):
    
    # preprocess
    transformed_sms = transform_text(input_sms)

    # vectorize
    vector_input = tfidf.transform([transformed_sms])

    # predict
    result = model.predict(vector_input)[0]
    prob = model.predict_proba(vector_input)

    st.write("Ham probability:", round(prob[0][0]*100,2),"%")
    st.write("Spam probability:", round(prob[0][1]*100,2),"%")

    if result == 1:
        st.error("Spam")
    else:
        st.success("Not Spam")