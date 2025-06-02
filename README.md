---
tags:
- hearthstone
- nlp
- text-classification
- game
- logistic-regression
---

# 🃏 Hearthstone Kart Sınıfı Tahmini (NLP)

Bu proje, kart açıklamasına göre Hearthstone kartlarının ait olduğu sınıfı (örneğin: Mage, Hunter, Neutral) tahmin eder.

## 📦 Kullanılan Veri Seti

- [Hearthstone Cards Dataset (Kaggle)](https://www.kaggle.com/datasets/jeradrose/hearthstone-cards)

## 🔍 Yöntem

- Kart açıklamaları temizlenip TF-IDF ile vektörleştirildi.
- Logistic Regression modeli ile sınıflandırma yapıldı.
- Başarı oranı: ~%61

## 🚀 Kullanım

```bash
streamlit run app.py

📁 Dosyalar
hearthstone_model.pkl

tfidf_vectorizer.pkl

app.py

requirements.txt

README.md