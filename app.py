import streamlit as st
import pickle
import nltk
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)
model = pickle.load(open("model2.pkl", "rb"))
tfidf=pickle.load(open("vectorizer2.pkl", "rb"))
st.title("Spam Detector")

text = st.text_area("Enter Message")


if st.button("Predict"):
    msg = transform_text(text)
    tfidf_msg = tfidf.transform([msg])
    result = model.predict(tfidf_msg)[0]

    if result == 1:
        st.error("Spam")
    else:
        st.success("Not Spam")
