import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_autor, refractor_idioma
from services import libro_service, autor_libro_service
from scraper import casa_del_libro
import datetime as dt

def autorellenado():
    soup, url = casa_del_libro.get_soup(isbn=isbn)
    if soup:
        titulo = casa_del_libro.get_titulo(soup)
        autores = casa_del_libro.get_autores(soup)
        ficha = casa_del_libro.extract_ficha_tecnica(soup)
        if titulo and ficha:
            datos = {
                "titulo": titulo,
                "autores": autores,
                "editorial": ficha.get("Editorial", "").split(":", 1)[1].strip(),
                "idioma": refractor_idioma(ficha.get("Idioma", "").split(":", 1)[1].strip()),
                "num_pag": int(ficha.get("Número de páginas", "0").split(":", 1)[1].strip()),
                "fecha_public": dt.datetime.strptime(ficha.get("Fecha de lanzamiento", "").split(":", 1)[1].strip(),"%d/%m/%Y").date()
            }
            st.write(datos)

# ==========================================================================================================

st.set_page_config(
    page_title="Nuevo Libro"
)

st.write("# ➕ Nuevo libro")

st.session_state["editando_libro"] = True

titulo = st.text_input("Título")

isbn = st.text_input("ISBN")
if st.button("Autorellenar a partir del isbn", icon=":material/search:"):
    autorellenado()

id_autores = select_autor()

id_saga = select_saga()

col1, col2, col3, col4, col5 = st.columns([0.15, 0.15, 0.4, 0.15, 0.15])
with col1:
    num_pag = st.text_input("Nº páginas")
    if num_pag:
        num_pag = int(num_pag)
    else:
        num_pag = None
with col2:
    idioma = select_idioma()
with col3:
    editorial = st.text_input("Editorial")
with col4:
    st.write("Wishlistear")
    with st.container(horizontal=True, horizontal_alignment="center"):
        en_wishlist = st.toggle("")
with col5:
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
