import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_autor, refractor_idioma, select_orden_saga
from services import libro_service, autor_libro_service, autor_service
from scraper import casa_del_libro
import datetime as dt

def autorellenado():

    # Reseteo de states
    for campo in ["titulo", "editorial", "idioma", "num_pag", "fecha_public", "url_portada"]:
        st.session_state[campo] = None
    st.session_state["autores"] = []
    st.session_state["autores_detectados"] = []

    # Extracción de datos
    soup, url = casa_del_libro.get_soup(isbn=st.session_state["isbn"])

    if soup:
        titulo = casa_del_libro.get_titulo(soup)
        autores = casa_del_libro.get_autores(soup)
        ficha = casa_del_libro.extract_ficha_tecnica(soup)

        if titulo and ficha:
            editorial = extraer_datos_ficha(ficha, "Editorial")
            idioma = extraer_datos_ficha(ficha, "Idioma")
            num_pag = extraer_datos_ficha(ficha, "Número de páginas")
            fecha_public = extraer_datos_ficha(ficha, "Fecha de lanzamiento")

            try:
                num_pag = int(num_pag) if num_pag else None
            except ValueError:
                num_pag = None

            datos = {
                "titulo": titulo,
                "autores": autores,
                "editorial": editorial,
                "idioma": refractor_idioma(idioma) if idioma else None,
                "num_pag": num_pag,
                "fecha_public": extraer_fecha(fecha_public),
                "url_portada": casa_del_libro.get_url_portada(soup)
            }

            # Seteo de states
            st.session_state["autores_detectados"] = autores
            autores_bbdd = autor_service.get_all_autores()
            nombres_scraper = [nombre.casefold() for nombre in autores]
            st.session_state["autores"] = [
                autor for autor in autores_bbdd
                if autor.nom_autor.casefold() in nombres_scraper
            ]
            for campo in ["titulo", "editorial", "idioma", "num_pag", "fecha_public", "url_portada"]:
                valor = datos[campo]
                st.session_state[campo] = (
                    str(valor) if campo == "num_pag" and valor is not None else valor
                )

        else:
            st.warning("No se han podido extraer los datos del libro.")

    else:
        st.warning("No se ha encontrado el libro.")

def extraer_datos_ficha(ficha, campo: str) -> str | None:
    valor = ficha.get(campo, "")
    if not valor or ":" not in valor:
        return None
    return valor.split(":", 1)[1].strip() or None

def extraer_fecha(valor: str | None) -> dt.date | None:
    if not valor:
        return None
    try:
        return dt.datetime.strptime(valor, "%d/%m/%Y").date()
    except ValueError:
        return None
        

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
    st.caption(f"Autores detectados: {', '.join(autores_detectados)}. Si alguno no está añadido en 'Autores', hay que añadirlo antes")
else:
    st.caption("Si algún autor no está añadido en 'Autores', hay que añadirlo antes")

col1, col2 = st.columns([0.8, 0.2])
with col1:
    id_saga = select_saga()
with col2:
    orden_saga = select_orden_saga(id_saga)

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
    prioridad_wishlist = select_prioridad_wishlist(en_wishlist=en_wishlist)

url_portada = st.text_input("Portada", key="url_portada", placeholder="URL")

fecha_public = select_date("Fecha de publicación", key="fecha_public")

generos = ",".join(select_genero())

sinopsis = add_texto("Sinopsis")

if st.button("Guardar", icon="💾"):
    libro_created = libro_service.create(
        id_saga=id_saga,
        titulo=titulo,
        isbn=isbn,
        orden_saga=orden_saga,
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