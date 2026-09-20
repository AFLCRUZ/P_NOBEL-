import numpy as np
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

st.write(''' # Predicción de categoría de Premio Nobel ''')
st.image("Nobel.png", caption="Su creador fue el inventor sueco Alfred Nobel mediante su testamento en 1895.")

st.header('Texto')

def cargar_modelo():
    # Carga tu dataset (asegúrate de que el nombre del archivo csv sea correcto)
    nobel = pd.read_csv('nobel_join.csv', encoding='latin-1')
    X = df.Label
    y = df.Category 
    
    # Vectorización con TF-IDF (igual que en tu prueba exitosa)
    vectorizer = TfidfVectorizer(max_features=1000)
    X_vec = vectorizer.fit_transform(X)
    
    # Entrenamiento con Regresión Logística
    model = LogisticRegression(random_state=42)
    model.fit(X_vec, y)
    
    return vectorizer, model

vectorizer, model = cargar_modelo()

def user_input_features():
    texto = st.text_input("Introduce el texto a evaluar")
    user_input_data = {'Label': [texto]}
    features = pd.DataFrame(user_input_data)
    return features

df = user_input_features()

st.subheader('Predicción')

if df['Label'].iloc[0].strip() != "":
    df_dtm = vect.transform(df['Label'])
    prediction = nb.predict(df_dtm)
    pred_val = prediction[0]
    
    if pred_val == 0:
        st.write('Physics')
    elif pred_val == 1:
        st.write('Medicine')
    elif pred_val == 2:
        st.write('Peace')
    elif pred_val == 3:
        st.write('Literature')
    elif pred_val == 4:
        st.write('Chemistry')
    elif pred_val == 5:
        st.write('Economics')
    else:
        st.write('Sin predicción')
else:
    st.info("Por favor, introduce un texto para ver la predicción.")
