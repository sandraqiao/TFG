import streamlit as st
from services import libro_service, autor_libro_service, saga_service
from utils.prints import *

def sort_biblioteca(sort_by, libros):
    if sort_by == constants.SORT_BIBLIOTECA[0]:
        # por titulo
        libros.sort(key=lambda libro: libro.titulo)
    elif sort_by == constants.SORT_BIBLIOTECA[1]:
        # por saga
        libros.sort(key=lambda libro: saga_service.get_saga(libro.id_saga).nom_saga)
    return libros

# ==========================================================================================================

st.set_page_config(
    page_title="Biblioteca"
)

st.write("# 📖 Biblioteca")

# # STATES EDICIONES
if st.session_state.get("libro_creado", False):
    st.toast("✔️ Libro creado correctamente")
    del st.session_state["libro_creado"]

if st.session_state.get("libro_editado", False):
    st.toast("✔️ Libro editado correctamente")
    del st.session_state["libro_editado"]

if st.session_state.get("libro_eliminado", False):
    st.toast("✔️ Libro eliminado correctamente")
    del st.session_state["libro_eliminado"]

if "editando_libro" not in st.session_state:
    st.session_state["editando_libro"] = False


# FILTER, SORT Y ADD LIBROS
with st.container(horizontal=True, horizontal_alignment="right"):
    with st.popover("", icon=":material/filter_alt:"):
        # filtro_popover()
        st.write("filtro")

    sort_by = st.menu_button("", icon=":material/sort:", options=constants.SORT_BIBLIOTECA)
    if sort_by is None:
        sort_by = constants.SORT_BIBLIOTECA[0]

    if st.button("", icon=":material/add:"):
        st.switch_page("./pages/add_libro.py")
        st.write("add libro")

# GET LIBROS A MOSTRAR
filtros = st.session_state.get("filtros_libros", None)
if filtros:
    libros = sort_biblioteca(sort_by, libro_service.filter_libro(generos=filtros["generos"], idiomas=filtros["idiomas"], editoriales=filtros["editoriales"], en_wishlist=filtros["en_wishlist"]))
else:
    libros = sort_biblioteca(sort_by, libro_service.get_all_libros())

# LISTADO DE LIBROS
if not libros:
    st.write("## 🕸️ No hay libros registrados 🕸️")

else:
    cols = st.columns(4)
    for i, libro in enumerate(libros):
        autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

        # IMPRESIONES
        with cols[i%4]:
            with st.container(border=True):
                with st.container(height=70, horizontal=True, horizontal_alignment="right", border=False):
                    col01, col02 = st.columns([5, 1])
                    with col01:
                        st.write(libro.titulo)
                    with col02:
                        if st.button("", icon=":material/info:", key=f"info_{libro.id_libro}", type="tertiary"):
                            st.session_state["info_libro_id"] = libro.id_libro
                            st.switch_page("./pages/edit_libro.py")
                            st.write("info")
                with st.container(height=220, horizontal_alignment="center", border=False):
                    if libro.url_portada:
                        st.image(libro.url_portada, width=150)
                    else:
                        st.caption("[Sin portada]")