import streamlit as st
from services import historico_precio_service, libro_service, autor_libro_service
from utils.prints import titulo_autor
from scraper.casa_del_libro import get_soup, extract_data_precios


def scrap(libros: list, historico: list):

    for libro in libros:

        url_libro = None

        historicos_libro = [h for h in historico if h.id_libro == libro.id_libro]
        for h in historicos_libro:
            if libro.isbn in h.url_libro and not url_libro:
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
            id_tienda=1,
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

libros = sorted([libro for libro in libro_service.get_all_libros() if libro.en_wishlist], 
                key=lambda libro: libro.titulo)
historico = sorted(historico_precio_service.get_all_historico_precio(), key=lambda historico: historico.id_libro)

if st.button("Scrapear", icon="🔍"):
    with st.spinner("Scrapeando precios..."):
        scrap(libros, historico)
        st.rerun()

for libro in libros:
    autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

    with st.container(border=True):
        st.write(titulo_autor(libro.titulo, autores))

        with st.expander("Casa del Libro"):

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