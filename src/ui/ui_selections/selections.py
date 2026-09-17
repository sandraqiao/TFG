import streamlit as st
from utils import constants
from utils.prints import *
from datetime import date
from services import libro_service, autor_libro_service

def retrieve_libro_index(libros: list, edit_libro_id: int):
    for i, libro in enumerate(libros):
        if libro.id_libro == edit_libro_id:
            return i

def select_libro(edit_libro_id: int | None = None) -> int:
    libros = sorted(libro_service.get_all_libros(), key=lambda libro: libro.titulo)
    selection = st.selectbox(
        "Título leído",
        libros,
        format_func=lambda libro: titulo_autor(libro.titulo, autor_libro_service.get_autores_by_libro(libro.id_libro)),
        index=retrieve_libro_index(libros, edit_libro_id) if edit_libro_id else 0
    )
    return selection.id_libro

def select_estado(edit_estado: str | None = None) -> str:
    estado = st.radio(
        "Estado actual de la lectura",
        constants.ESTADO,
        index=constants.ESTADO.index(edit_estado) if edit_estado else 0
    )
    return estado

def select_formato(edit_formato: str | None = None) -> str:
    return st.radio(
        "Formato",
        constants.FORMATO,
        index=constants.FORMATO.index(edit_formato) if edit_formato else 0
    )

# def select_genero() -> list:
#     generos = st.pills(
#         "Géneros:",
#         constants.GENERO,
#         selection_mode="multi"
#     )
#     return generos

def select_valoracion(edit_valoracion: int | None = None) -> int:
    valoracion = st.feedback(
        "stars",
        default=edit_valoracion - 1 if edit_valoracion is not None else None
    )
    return valoracion + 1 if valoracion is not None else None

def select_date(tipo: str, edit_fecha: date | None = None) -> date:
    return st.date_input(
        tipo,
        value = edit_fecha or None, 
        format="DD/MM/YYYY"
    )

def add_comentario(edit_comentario: str | None = None) -> str:
    return st.text_area(
        "Comentario",
        placeholder=edit_comentario or None
    )
