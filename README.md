# 📧 Email Spam Detection

A Machine Learning web application that classifies email messages as **Spam** or **Legitimate** using Natural Language Processing (NLP) techniques. The application is built using Python, Scikit-learn, NLTK, and Streamlit, and is deployed as an interactive web application.

## 🚀 Live Demo

🔗 Add your deployed Streamlit URL here:

https://emailspamdetection-ad7yj3n7xjcikfigteb6jr.streamlit.app/

---

## 📌 Features

* Detects Spam and Legitimate Emails
* NLP-based text preprocessing
* TF-IDF Vectorization
* Machine Learning-based Classification
* Confidence Score Display
* Interactive Streamlit User Interface
* Real-time Prediction

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK
* Pandas
* NumPy
* Pickle

---

## 🤖 Machine Learning Workflow

1. Text Cleaning
2. Lowercase Conversion
3. Tokenization using NLTK
4. Stopword Removal
5. Stemming using Porter Stemmer
6. TF-IDF Vectorization
7. Model Training
8. Prediction and Classification

---

## 📊 Model Selection & Evaluation

Multiple machine learning models were trained and evaluated to identify the best-performing classifier for spam detection.

### Models Evaluated

* Multinomial Naive Bayes
* Logistic Regression
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* XGBoost Classifier
* Voting Classifier
* Stacking Classifier

### Evaluation Metrics

The models were compared using:

* Accuracy
* Precision Score

For spam detection systems, **Precision** is one of the most important metrics because incorrectly classifying legitimate emails as spam can negatively impact users.

After evaluating all models, **Multinomial Naive Bayes** combined with **TF-IDF Vectorization** provided the best balance between accuracy and precision on the dataset and was selected as the final production model.

### Final Model

* Algorithm: Multinomial Naive Bayes
* Feature Extraction: TF-IDF Vectorizer
* Text Preprocessing: NLTK
* Deployment: Streamlit Cloud

---

## 📂 Project Structure

```text
EmailSpamDetection/
│
├── app.py
├── model2.pkl
├── vectorizer2.pkl
├── requirements.txt
├── README.md
└── spam.csv
```

---

## ▶️ Run Locally

### Clone the Repository

```bash
git clone <repository-url>
cd EmailSpamDetection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots of your application here.

### Home Page

Upload screenshot and replace this section.

### Prediction Result

Upload screenshot and replace this section.

---

## 🎯 Use Cases

* Email Spam Filtering
* Text Classification Projects
* NLP Learning Projects
* Machine Learning Deployment Practice
* Academic and Portfolio Demonstrations

---

## 🌟 Future Improvements

* Deep Learning-based Spam Detection
* Email Subject & Body Analysis
* Multiple Language Support
* Enhanced UI/UX
* Cloud Database Integration
* User Authentication

---

## 👨‍💻 Author

**Chandandrakanth Dodapaneni**

Built using Machine Learning, NLP, and Streamlit.

If you found this project useful, consider giving it a ⭐ on GitHub.
