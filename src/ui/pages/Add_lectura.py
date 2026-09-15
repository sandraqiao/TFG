import streamlit as st
from services import lectura_service, libro_service, autor_libro_service
from utils.prints import *

def select_libro() -> int:
    libros = sorted(libro_service.get_all_libros(), key=lambda libro: libro.titulo)

    selection = st.selectbox(
        "Título leído:",
        libros,
        format_func=lambda libro: titulo_autor(libro.titulo, autor_libro_service.get_autores_by_libro(libro.id_libro))
    )

    return selection




st.set_page_config(
    page_title="Add_lectura"
)

st.write("# ➕ Nueva Lectura")

libro = select_libro()
st.write(f"{libro.id_libro}: {libro.titulo}")