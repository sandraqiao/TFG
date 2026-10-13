import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_autor, refractor_idioma
from services import libro_service, autor_libro_service, autor_service
from scraper import casa_del_libro
import datetime as dt

def autorellenado():

    # reset de states
    for campo in ["titulo", "editorial", "idioma", "num_pag", "fecha_public", "url_portada", "autores"]:
        st.session_state[campo] = None

    # extracción de datos
    soup, url = casa_del_libro.get_soup(isbn=st.session_state["isbn"])
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
                "fecha_public": dt.datetime.strptime(ficha.get("Fecha de lanzamiento", "").split(":", 1)[1].strip(), "%d/%m/%Y").date(),
                "url_portada": casa_del_libro.get_url_portada(soup)
            }
            st.write(datos)

            # seteo de states
            st.session_state["autores_detectados"] = autores
            autores_bbdd = autor_service.get_all_autores()
            nombres_scraper = [nombre.casefold() for nombre in autores]
            st.session_state["autores"] = [autor for autor in autores_bbdd if autor.nom_autor.casefold() in nombres_scraper]

            for campo in ["titulo", "editorial", "idioma", "num_pag", "fecha_public", "url_portada"]:
                st.session_state[campo] = str(datos[campo]) if campo == "num_pag" and datos[campo] is not None else datos[campo]
    
    else:
        st.warning("No se ha encontrado el libro.")

# ==========================================================================================================

st.set_page_config(
    page_title="Nuevo Libro"
)

st.write("# ➕ Nuevo libro")

titulo = st.text_input("Título", key="titulo")

isbn = st.text_input("ISBN", key="isbn")
st.button("Autorellenar a partir del isbn", icon=":material/search:", on_click=autorellenado)

id_autores = select_autor()
autores_detectados = st.session_state.get("autores_detectados") or []
if autores_detectados:
    st.caption(f"Autores detectados: {', '.join(autores_detectados)}. Si alguno no está añadido en 'Autores', hay que añadirlo antes.")
else:
    st.caption("Si alguno no está añadido en 'Autores', hay que añadirlo antes.")

id_saga = select_saga()

col1, col2, col3, col4, col5 = st.columns([0.15, 0.15, 0.4, 0.15, 0.15])
with col1:
    num_pag = st.text_input("Nº páginas", key="num_pag")
    if num_pag:
        num_pag = int(num_pag)
    else:
        num_pag = None
with col2:
    idioma = select_idioma()
with col3:
    editorial = st.text_input("Editorial", key="editorial")
with col4:
    st.write("Wishlistear")
    with st.container(horizontal=True, horizontal_alignment="center"):
        en_wishlist = st.toggle("")
with col5:
    prioridad_wishlist = select_prioridad_wishlist()

generos = ",".join(select_genero())

url_portada = st.text_input("Portada", key="url_portada", placeholder="URL")

fecha_public = select_date("Fecha de publicación", key="fecha_public")

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

    st.session_state["autores_detectados"] = []
    st.session_state["libro_creado"] = True
    st.switch_page("./pages/biblioteca.py")