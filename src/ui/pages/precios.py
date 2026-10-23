import streamlit as st
from services import historico_precio_service, libro_service, autor_libro_service
from utils.prints import titulo_autor
from scraper.casa_del_libro import get_soup, extract_data_precios
import datetime as dt
from utils.constants import TIENDA_SCRAPER


def scrap(libros: list, historico: list):
    hoy = dt.date.today()

    for libro in libros:

        historicos_libro = [h for h in historico if h.id_libro == libro.id_libro]

        if any(h.fecha_consulta == hoy for h in historicos_libro):
                    continue

        url_libro = None

        for h in historicos_libro:
            if libro.isbn and h.url_libro and libro.isbn in h.url_libro and not url_libro:
                url_libro = h.url_libro

        if url_libro:
            soup, url_libro = get_soup(url = url_libro)
        else:
            soup, url_libro = get_soup(isbn=libro.isbn)

        if soup is None:
            continue
        
        scraped_data = extract_data_precios(soup)

        historico_precio_service.create(
            id_libro=libro.id_libro,
            nom_tienda=TIENDA_SCRAPER[0],
            precio=scraped_data["precio"],
            fecha_consulta=scraped_data["fecha_consulta"],
            disponible=scraped_data["disponible"],
            url_libro=url_libro,
            pct_descuento=scraped_data["pct_descuento"]
        )

# ==========================================================================================================

st.set_page_config(
    page_title="Precios"
)

st.write("# 💰 Histórico de precios")

libros = sorted([libro for libro in libro_service.get_all_libros() if libro.en_wishlist], key=lambda libro: libro.titulo)
historico = sorted(historico_precio_service.get_all_historico_precio(), key=lambda historico: historico.id_libro)
libros_sin_busqueda = [libro for libro in libros if not libro.isbn and not any(h.id_libro == libro.id_libro for h in historico)]

if libros_sin_busqueda:
    aux = len(libros_sin_busqueda)
    if aux == 1: 
        st.info(f"Hay {aux} libro de tu wishlist sin ISBN ni URL de una consulta anterior, luego no se podrá realizar una búsqueda automática en La Casa del Libro.")
    if aux > 1:
        st.info(f"Hay {aux} libros de tu wishlist sin ISBN ni URL de una consulta anterior, luego no se podrá realizar una búsqueda automática en La Casa del Libro.")

if st.button("Scrapear", icon="🔍"):
    with st.spinner("Scrapeando precios..."):
        scrap(libros, historico)
        st.rerun()

for libro in libros:
    autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

    with st.container(border=True):
        st.write(titulo_autor(libro.titulo, autores))

        with st.expander(TIENDA_SCRAPER[0]):

            historicos_libro = [h for h in historico if h.id_libro == libro.id_libro]
            tabla_datos = []

            for h in historicos_libro:
                tabla_datos.append({
                    "Fecha": h.fecha_consulta.strftime("%d/%m/%Y"),
                    "Precio": f"{h.precio:.2f}",
                    "Descuento": f"{h.pct_descuento:.0f} %" if h.pct_descuento is not None else "-",
                    "Disponible": "🟢" if h.disponible else "🔴"
                })

            st.dataframe(tabla_datos, hide_index=True, use_container_width=True)