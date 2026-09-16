import streamlit as st
from utils import constants
from utils.prints import *
from datetime import date
from services import libro_service, autor_libro_service

def select_libro() -> int:
    libros = sorted(libro_service.get_all_libros(), key=lambda libro: libro.titulo)
    selection = st.selectbox(
        "Título leído",
        libros,
        format_func=lambda libro: titulo_autor(libro.titulo, autor_libro_service.get_autores_by_libro(libro.id_libro))
    )
    return selection.id_libro

def select_estado() -> str:
    estado = st.radio(
        "Estado actual de la lectura",
        constants.ESTADO
    )
    return estado

def select_formato() -> str:
    formato = st.radio(
        "Formato",
        constants.FORMATO
    )
    return formato

# def select_genero() -> list:
#     generos = st.pills(
#         "Géneros:",
#         constants.GENERO,
#         selection_mode="multi"
#     )
#     return generos

def select_valoracion() -> int:
    valoracion = st.feedback(
        "stars",
        default=None
    )
    return valoracion

def select_date(tipo: str) -> date:
    d = st.date_input(
        tipo,
        value = None, 
        format="DD/MM/YYYY"
    )
    return d

def add_comentario() -> str:
    comentario = st.text_area(
        "Comentario"
    )
    return comentario