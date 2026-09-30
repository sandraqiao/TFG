import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_autor
from services import libro_service, autor_libro_service
from scraper import casa_del_libro
  

# ==========================================================================================================

st.set_page_config(
    page_title="Nuevo Libro"
)

st.write("# ➕ Nuevo libro")

st.session_state["editando_libro"] = True

titulo = st.text_input("Título")

id_autores = select_autor()

id_saga = select_saga()

col11, col12, col13 = st.columns([0.5, 0.15, 0.35])
col21, col22, col23 = st.columns([0.5, 0.15, 0.35])
with col11:
    isbn = st.text_input("ISBN")
with col12:
    idioma = select_idioma()
with col13:
    editorial = st.text_input("Editorial")
with col21:
    num_pag = st.text_input("Número de páginas")
    if num_pag:
        num_pag = int(num_pag)
    else:
        num_pag = None
with col22:
    st.write("Wishlistear")
    with st.container(horizontal=True, horizontal_alignment="center"):
        en_wishlist = st.toggle("")
with col23:
    prioridad_wishlist = select_prioridad_wishlist()

generos = ",".join(select_genero())

url_portada = st.text_input("Portada", placeholder="URL")

fecha_public = select_date("Fecha de publicación")

sinopsis = add_texto("Sinopsis")

if st.button("Guardar", icon="💾"):
    libro_created = libro_service.create(
        id_saga=id_saga,
        titulo=titulo,
        isbn=isbn,
        num_pag=num_pag,
        genero=generos,
        idioma=idioma,
        sinopsis=sinopsis,
        fecha_public=fecha_public,
        url_portada=url_portada,
        editorial=editorial,
        en_wishlist=en_wishlist,
        prioridad_wishlist=prioridad_wishlist,
    )

    for id in id_autores:
        autor_libro_service.create(libro_created.id_libro, id)
        
    st.session_state["editando_libro"] = False
    st.session_state["libro_creado"] = True
    st.switch_page("./pages/biblioteca.py")


# if isbn:
#     if st.button("Autorellenar a partir del isbn", icon=":material/search:"):
#         st.write("autorellenar")
#         url = casa_del_libro.extract_url_por_isbn(isbn)
#         st.write(url)