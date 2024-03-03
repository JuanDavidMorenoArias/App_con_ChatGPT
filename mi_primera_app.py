# Importar la biblioteca Streamlit
import streamlit as st

# Título y autor
st.title("Mi primera app")
st.text("Esta app fue elaborada por Juan David Moreno Arias")

# Preguntar al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Saludo personalizado
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")