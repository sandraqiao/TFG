import streamlit as st
from services import libro_service, lectura_service
from utils import constants
from collections import Counter


def get_stats_libros(libros):
    total = len(libros)
    en_wishlist = sum(1 for libro in libros if libro.en_wishlist)
    sagas = len(set(libro.id_saga for libro in libros if libro.id_saga is not None))
    return total, en_wishlist, sagas


def get_stats_lecturas(lecturas):
    total = len(lecturas)

    leyendo = sum(1 for lectura in lecturas if lectura.estado == constants.ESTADO[0])
    leidas = sum(1 for lectura in lecturas if lectura.estado == constants.ESTADO[1])
    abandonadas = sum(1 for lectura in lecturas if lectura.estado == constants.ESTADO[2])
    valoraciones = [lectura.valoracion for lectura in lecturas if lectura.valoracion is not None]
    valoracion_media = (sum(valoraciones) / len(valoraciones) if valoraciones else None)

    return total, leyendo, leidas, abandonadas, valoracion_media


def get_generos(libros):
    generos = []
    for libro in libros:
        if libro.genero:
            generos.extend(genero.strip() for genero in libro.genero.split(","))
    return Counter(generos)


def get_formatos(lecturas):
    formatos = Counter()
    for lectura in lecturas:
        formatos[lectura.formato] += 1
    return formatos


def get_valoraciones(lecturas):
    valoraciones = Counter()
    for lectura in lecturas:
        if lectura.valoracion is not None:
            valoraciones[lectura.valoracion] += 1
    return valoraciones


def get_lecturas_por_año(lecturas):
    años = Counter()
    for lectura in lecturas:
        if lectura.fecha_fin is not None:
            años[lectura.fecha_fin.year] += 1
    return años

# ==========================================================================================================

st.set_page_config(
    page_title="Estadísticas"
)

st.write("# 📊 Estadísticas")

# VARIABLES IMPORTANTES
libros = libro_service.get_all_libros()
lecturas = lectura_service.get_all_lecturas()

total_libros, en_wishlist, sagas = get_stats_libros(libros)
total_lecturas, leyendo, leidas, abandonadas, valoracion_media = get_stats_lecturas(lecturas)
lecturas_por_año = get_lecturas_por_año(lecturas)
valoraciones = get_valoraciones(lecturas)
generos = get_generos(libros)
formatos = get_formatos(lecturas)

# RESUMEN
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📖 Libros", total_libros)
with col2:
    st.metric("🔖 Lecturas", total_lecturas)
with col3:
    st.metric("❤️ Wishlist", en_wishlist)
with col4:
    st.metric("📚 Sagas", sagas)

st.divider()

# LECTURAS
st.write("## 📖 Lecturas")

with st.container(border=True):
    st.write("### Estado")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(f"{constants.ESTADO[0]}", leyendo)
    with col2:
        st.metric(f"{constants.ESTADO[1]}", leidas)
    with col3:
        st.metric(f"{constants.ESTADO[2]}", abandonadas)

with st.container(border=True):
    st.write("### Valoraciones")
    valoraciones = {
        f"{valoracion} ⭐": valoraciones.get(valoracion, 0)
        for valoracion in range(constants.VALORACION_MIN, constants.VALORACION_MAX + 1)
    }
    st.bar_chart(valoraciones)
    if valoracion_media is not None:
        st.write(
            f"**Valoración media: {valoracion_media:.2f} ⭐**"
        )

st.divider()

# EVOLUCIÓN
st.write("## 📈 Evolución de lectura")
if lecturas_por_año:
    años = range(min(lecturas_por_año), max(lecturas_por_año) + 1)
    lecturas_por_año = {año: lecturas_por_año.get(año, 0) for año in años}
    st.line_chart(lecturas_por_año)
else:
    st.write("Todavía no hay lecturas finalizadas.")

st.divider()

# BIBLIOTECA
st.write("## 📚 Biblioteca")

with st.container(border=True):
    st.write("### Formatos")
    col1, col2, col3 = st.columns(3)
    for i, formato in enumerate(constants.FORMATO):
        with [col1, col2, col3][i]:
            st.metric(formato, formatos.get(formato, 0))

with st.container(border=True):
    st.write("### Géneros")
    if generos:
        st.bar_chart(generos)
    else:
        st.write("No hay géneros registrados.")