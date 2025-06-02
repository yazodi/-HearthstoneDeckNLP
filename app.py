
# app.py
import streamlit as st
import joblib

# Model ve vektör yükle
model = joblib.load("hearthstone_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Temizlik fonksiyonları
import re, string

def clean_html(text):
    return re.sub(r"<.*?>", "", str(text))

def preprocess_text(text):
    text = clean_html(text)
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def predict_class(text):
    cleaned = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned])
    return model.predict(vectorized)[0]

# Streamlit Arayüzü
st.title("🃏 Hearthstone Kart Sınıfı Tahmin Aracı")

kart_aciklama = st.text_area("Kart Açıklamasını Girin")

if st.button("Sınıfı Tahmin Et"):
    if kart_aciklama.strip():
        tahmin = predict_class(kart_aciklama)
        st.success(f"🎯 Tahmin Edilen Kart Sınıfı: **{tahmin}**")
    else:
        st.warning("Lütfen bir açıklama girin.")
