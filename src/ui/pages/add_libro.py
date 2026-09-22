import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist
from services import libro_service
from scraper import casa_del_libro

st.set_page_config(
    page_title="Nuevo Libro"
)

st.write("# ➕ Nuevo libro")

titulo = st.text_input("Título")
# st.write(titulo)
saga = select_saga()
# st.write(saga)

col01, col02, col03 = st.columns([0.5, 0.15, 0.35])
col11, col12, col13 = st.columns([0.5, 0.15, 0.35])
with col01:
    isbn = st.text_input("ISBN")
with col02:
    idioma = select_idioma()
with col03:
    editorial = st.text_input("Editorial")
with col11:
    num_pags = st.text_input("Número de páginas")
with col12:
    st.write("Wishlistear")
    with st.container(horizontal=True, horizontal_alignment="center"):
        en_wishlist = st.toggle("")
with col13:
    prioridad_wishlist = select_prioridad_wishlist()

generos = select_genero()
# st.write(generos)

url_portada = st.text_input("Portada", placeholder="URL")

fecha_public = select_date("Fecha de publicación")

sinopsis = add_texto("Sinopsis")


# if isbn:
#     if st.button("Autorellenar a partir del isbn", icon=":material/search:"):
#         st.write("autorellenar")
#         url = casa_del_libro.extract_url_por_isbn(isbn)
#         st.write(url)