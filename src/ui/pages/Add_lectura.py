import streamlit as st
from services import lectura_service, libro_service, autor_libro_service
from utils.prints import *
from utils import constants

def select_libro() -> int:
    libros = sorted(libro_service.get_all_libros(), key=lambda libro: libro.titulo)
    selection = st.selectbox(
        "Título leído",
        libros,
        format_func=lambda libro: titulo_autor(libro.titulo, autor_libro_service.get_autores_by_libro(libro.id_libro))
    )
    return selection

def select_estado() -> str:
    estado = st.radio(
        "Estado actual de la lectura",
        constants.ESTADO
    )
    return estado

def select_valoracion() -> int:
    valoracion = st.slider(
        "Valoración", 
        constants.VALORACION_MIN, 
        constants.VALORACION_MAX)
    return valoracion

def add_comentario() -> str:
    comentario = st.text_area(
        "Comentario"
    )
    st.write(f"{len(comentario)} caracteres")
    return comentario



# ==========================================================================================================

st.set_page_config(
    page_title="Add_lectura"
)

st.write("# ➕ Nueva Lectura")

libro = select_libro()
st.write(f"{libro.id_libro}: {libro.titulo}")

estado = select_estado()
st.write(f"estado: {estado}")

valoracion = select_valoracion()
st.write(f"valoracion: {valoracion}")

comentario = add_comentario()
st.write(f"comentario: {comentario}")