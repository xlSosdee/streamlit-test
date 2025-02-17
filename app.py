import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests

st.write("Hola soy un comentario en streamlit")
st.text_input("Inserte aqui su nombre:")
st.button("Guardar")

# URL de la API de ExchangeRate.host (sin necesidad de API Key)
url = "https://api.exchangerate.host/latest?base=USD"

# Hacer la solicitud GET
response = requests.get(url).json()

# Mostrar la respuesta en Streamlit
st.json(response)