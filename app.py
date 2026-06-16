import streamlit as st
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)
import pickle
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
@st.cache_resource
def load_models():
    model = pickle.load(open("model2.pkl", "rb"))
    tfidf = pickle.load(open("vectorizer2.pkl", "rb"))
    return model, tfidf

model, tfidf = load_models()


st.title("📧 Email Spam Detector")
st.markdown("Detect whether an email is **Spam** or **Not Spam** using Machine Learning.")

st.divider()

text = st.text_area(
    "Enter Email Message",
    height=200,
    placeholder="Paste your email content here..."
)

if st.button("🔍 Analyze Email", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter an email message.")
    else:

        msg = transform_text(text)

        vector_input = tfidf.transform([msg])
        result = model.predict(vector_input)[0]
        prob = model.predict_proba(vector_input)
        confidence = max(prob[0]) * 100

        st.divider()
        st.info(f"Confidence Score: {confidence:.2f}%")

        if result == 1:
            st.error("🚨 Spam Email Detected")
        else:
            st.success("✅ Legitimate Email")


st.markdown("---")

with st.expander("📌 About This Project"):
    st.write("""
    **Technologies Used**

    - TF-IDF Vectorizer
    - Multinomial Naive Bayes
    - NLTK Text Preprocessing
    - Streamlit

    This application predicts whether an email is Spam or Legitimate.
    """)
