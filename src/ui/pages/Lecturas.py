import streamlit as st
from datetime import date
from services import lectura_service, libro_service, autor_service, autor_libro_service

# ==========================================================================================================

def titulo_y_autor(id_libro: int) -> str:

    libro = libro_service.get_libro(id_libro)
    autoreslibro = autor_libro_service.search_by_libro(libro.id_libro)

    titulo_y_autor = libro.titulo
    
    for autorlibro in autoreslibro:
        titulo_y_autor += " - "
        titulo_y_autor += autor_service.get_by_id(autorlibro.id_autor).nom_autor

    return titulo_y_autor

def codigo_estado(estado: str) -> str:

    if estado == "Leído":
        return "🟢"
    elif estado == "Leyendo":
        return "🟡"
    else:
        return "🔴"

def estrellas(valoracion: int) -> str:
    estrellas = ""

    if valoracion:
        for i in range(10):
            if i < valoracion:
                estrellas += "★"
            else:
                estrellas += "☆"
            estrellas += " "
    else:
        estrellas = "☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆"
        valoracion = 0

    estrellas += f"({valoracion}/10)"
    return estrellas

def fechas(ini: date, fin: date | None) -> str:

    fechas = ""

    if fin:
        fechas += f"{ini.strftime('%d/%m/%Y')} - {fin.strftime('%d/%m/%Y')}"
    else:
        fechas += f"{ini.strftime('%d/%m/%Y')} - [sin especificar]"

    return fechas

# ==========================================================================================================

st.set_page_config(
    page_title="Lecturas"
)

st.write("# 🔖 Lecturas")

lecturas = lectura_service.get_all_lecturas()

if lecturas is None:
    st.write("## 🕸️ No hay lecturas registradas 🕸️")

else:

    for lectura in lecturas:

        libro = libro_service.get_libro(lectura.id_libro)

        with st.expander(f"{codigo_estado(lectura.estado)} {titulo_y_autor(libro.id_libro)}"):

            col11, col12 = st.columns(2)
            with col11:
                st.write(f"Estado: {lectura.estado}")
            with col12:
                st.write(f"Formato: {lectura.formato}")

            col21, col22 = st.columns(2)
            with col21:
                st.write(f"Valoración: {estrellas(lectura.valoracion)}")
            with col22:
                st.write(f"{fechas(lectura.fecha_ini, lectura.fecha_fin)}")

            if lectura.comentario:
                st.write(f"{lectura.comentario}")

# ==========================================================================================================
