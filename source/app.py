import streamlit as st
import joblib
import numpy as np

# 📌 Cargar el modelo

#Entorno de desarrollo
# model = joblib.load(".\models\modelo_entrenado.pkl")


#Entorno de producción
model = joblib.load("models/modelo_entrenado.pkl")

st.title("Predicción con Modelo de Regresión Logística")

# 📌 Crear entradas para el usuario
sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1)

if st.button("Predecir"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    clases = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    st.write(f"🔍 Predicción: {clases[prediction[0]]}")
  