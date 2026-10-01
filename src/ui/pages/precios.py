import streamlit as st
from services import historico_precio_service, libro_service, autor_libro_service
from utils.prints import titulo_autor
from scraper.casa_del_libro import extract_url_por_isbn, extract_precio_data

def scrap(libros: list, historico: list):

    for libro in libros:

        url_libro = None

        historicos_libro = [h for h in historico if h.id_libro == libro.id_libro]
        for h in historicos_libro:
            if libro.isbn in h.url_libro and not url_libro:
                url_libro = h.url_libro
        if not url_libro:
            url_libro = extract_url_por_isbn(libro.isbn)
        
        scraped_data = extract_precio_data(url_libro)

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

for libro in libros:
    autores = autor_libro_service.get_autores_by_libro(libro.id_libro)
    with st.container(border=True):
        st.write(titulo_autor(libro.titulo, autores))
        with st.expander("Casa del Libro"):
            st.write("")