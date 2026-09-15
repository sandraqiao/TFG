import streamlit as st
from services import lectura_service, libro_service

st.set_page_config(
    page_title="Add_lectura"
)

st.write("# ➕ Nueva Lectura")

libros = libro_service.get_all_libros()
titulos = []

for libro in libros:
    titulos.append(libro.titulo)

libro = st.selectbox(
    "Título leído:",
    (sorted(titulos))
)