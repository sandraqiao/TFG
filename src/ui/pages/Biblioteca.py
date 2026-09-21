import streamlit as st
from services import libro_service, autor_libro_service
from utils.prints import *

# @st.dialog("Seguro que quieres borrar el libro?", dismissible=False, icon="⚠️")
# def confirm_delete(id_libro: int) -> bool:
#     st.write("Esta acción no se puede deshacer")

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Si, bórralo"):
#             libro_service.delete(id_libro)
#             st.session_state["libro_eliminado"] = True
#             st.rerun()
#     with col2:
#         if st.button("No, me arrepiento"):
#             st.rerun()

# def filtro_popover():
#     generos = filtrado(constants.FILTROS_LIBROS[0])
#     st.divider()
#     idiomas = filtrado(constants.FILTROS_LIBROS[1])
#     st.divider()
#     editoriales = filtrado(constants.FILTROS_LIBROS[2])
#     st.divider()
#     en_wishlist = filtrado(constants.FILTROS_LIBROS[3])

#     with st.container(horizontal=True, horizontal_alignment="right"):
#         if st.button("Aplicar"):
#             st.session_state["filtros_libros"] = {
#                 "generos": generos,
#                 "idiomas": idiomas,
#                 "editoriales": editoriales,
#                 "en_wishlist": en_wishlist
#             }
#             st.rerun()

# def retrieve_editoriales(): 
#     libros = libro_service.get_all_libros()
#     editoriales = []
#     for libro in libros:
#         if editoriales:
#             editoriales.append(libro.editorial)
#     return sorted(set(editoriales))


# def filtrado(to_filter: str):
#     if to_filter == constants.FILTROS_LIBROS[0]:
#         options = constants.GENERO
#     elif to_filter == constants.FILTROS_LIBROS[1]:
#         options = constants.IDIOMA
#     elif to_filter == constants.FILTROS_LIBROS[2]:
#         options = retrieve_editoriales()
#     elif to_filter == constants.FILTROS_LIBROS[3]:
#         options = ["Sí", "No"]

#     st.write(to_filter)

#     result = []
#     for i, option in enumerate(options):
#         actual = st.checkbox(f"{option}")
#         if actual:
#             result.append(f"{options[i]}")
#     return result

# ==========================================================================================================

st.set_page_config(
    page_title="Biblioteca"
)

st.write("# 📚 Biblioteca")

# # STATES EDICIONES
# if st.session_state.get("libro_creado", False):
#     st.toast("✔️ Libro creado correctamente")
#     del st.session_state["libro_creado"]

# if st.session_state.get("libro_editado", False):
#     st.toast("✔️ Libro editado correctamente")
#     del st.session_state["libro_editado"]

# if st.session_state.get("libro_eliminado", False):
#     st.toast("❌ Libro eliminado correctamente")
#     del st.session_state["libro_eliminado"]


# FILTER Y ADD LIBROS
with st.container(horizontal=True, horizontal_alignment="right"):
    with st.popover("", icon=":material/filter_alt:"):
        # filtro_popover()
        st.write("filtro")
    if st.button("", icon=":material/add:"):
        # st.switch_page("./pages/add_lectura.py")
        st.write("add libro")

# GET LIBROS A MOSTRAR
filtros = st.session_state.get("filtros_libros", None)
if filtros:
    libros = libro_service.filter_libro(generos=filtros["generos"], idiomas=filtros["idiomas"], editoriales=filtros["editoriales"], en_wishlist=filtros["en_wishlist"])
else:
    libros = libro_service.get_all_libros()

# LISTADO DE LIBROS
if libros is None:
    st.write("## 🕸️ No hay libros registrados 🕸️")
else:

    cols = st.columns(4)
    for i, libro in enumerate(libros):
        autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

        # IMPRESIONES
        with cols[i%4]:
            with st.container(width=150, height=275, border=True):
                with st.container(width=150, height=50, border=False):
                    st.write(libro.titulo)
                if libro.url_portada:
                    st.image(libro.url_portada, width=150)
                else:
                    st.caption("[Sin portada]")