import streamlit as st
from utils import constants
from utils.prints import *
from datetime import date
from services import libro_service, autor_libro_service, saga_service, autor_service

# ==========================================================================================================
# LIBRO
# ==========================================================================================================

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

def retrieve_saga_index(sagas: list, edit_saga_id: int):
    for i, saga in enumerate(sagas):
        if saga.id_saga == edit_saga_id:
            return i
        
def select_saga(edit_saga_id: int | None = None) -> int:
    sagas = sorted(saga_service.get_all_sagas(), key=lambda saga: saga.nom_saga)
    selection = st.selectbox(
        "Saga",
        [None] + sagas,
        format_func=lambda saga: saga.nom_saga if saga else "",
        index=retrieve_saga_index(sagas, edit_saga_id) + 1 if edit_saga_id else 0,
        disabled=not st.session_state["editando_libro"]
    )
    return selection.id_saga if selection else None


def select_autor(edit_autores_id: list | None = None) -> list[int]:
    autores = sorted(autor_service.get_all_autores(), key=lambda autor: autor.nom_autor)
    selection = st.multiselect(
        "Autor",
        autores,
        format_func=lambda autor: autor.nom_autor,
        default=[autor for autor in autores if edit_autores_id and autor.id_autor in edit_autores_id],
        disabled=not st.session_state["editando_libro"]
    )
    return [autor.id_autor for autor in selection]

def select_prioridad_wishlist(edit_prioridad: int | None = None) -> int:
    selection = st.selectbox(
        "Prioridad",
        [None] + list(range(constants.PRIORIDAD_WISHLIST_MIN, constants.PRIORIDAD_WISHLIST_MAX+1)),
        index=edit_prioridad if edit_prioridad else None,
        disabled=not st.session_state["editando_libro"]
    )
    return selection if selection else None

def select_idioma(edit_idioma: str | None = None) -> str:
    return st.selectbox(
        "Idioma",
        constants.IDIOMA,
        index=constants.ESTADO.index(edit_idioma) if edit_idioma else 0,
        disabled=not st.session_state["editando_libro"]
    )

def refractor_idioma(idioma: str):
    if idioma == "Castellano":
        return constants.IDIOMA[0]
    elif idioma == "":
        return constants.IDIOMA[1]
    else:
        return None

def select_genero(str_generos: str | None = None) -> list:
    inicial = str_generos.split(",") if str_generos else None
    generos = st.pills(
        "Géneros",
        constants.GENERO,
        selection_mode="multi",
        default=inicial if inicial else None,
        disabled=not st.session_state["editando_libro"]
    )
    return generos

def select_date(tipo: str, edit_fecha: date | None = None) -> date:
    return st.date_input(
        tipo,
        value = edit_fecha or None, 
        format="DD/MM/YYYY",
        disabled=not st.session_state["editando_libro"]
    )

def select_wishlist(en_wishlist: bool) -> bool:
    yes_no = ["Yes pliz", "Nah"]
    selection = st.selectbox(
        "Wishlistear",
        yes_no,
        index=0 if en_wishlist else 1,
        disabled=not st.session_state["editando_libro"]
    )
    return selection == yes_no[0]

def add_texto(tipo: str, edit_texto: str | None = None) -> str:
    return st.text_area(
        tipo,
        placeholder=edit_texto or None,
        disabled=not st.session_state["editando_libro"]
    )

# ==========================================================================================================
# LECTURA
# ==========================================================================================================

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

def select_valoracion(edit_valoracion: int | None = None) -> int:
    valoracion = st.feedback(
        "stars",
        default=edit_valoracion - 1 if edit_valoracion is not None else None
    )
    return valoracion + 1 if valoracion is not None else None