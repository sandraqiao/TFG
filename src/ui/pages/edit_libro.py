import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_wishlist
from services import libro_service, saga_service

@st.dialog("Seguro que quieres eliminar el libro?", dismissible=False, icon="⚠️")
def confirm_delete(id_libro: int) -> bool:
    st.write("Toda la información relacionada con este libro se eliminará junto a él.")
    st.caption("Lecturas, históricos de precios y relaciones entre autor y libro donde participe este libro")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Lo entiendo, bórralo aún así"):
            libro_service.delete(id_libro)
            st.session_state["libro_eliminado"] = True
            st.switch_page("./pages/biblioteca.py")
    with col2:
        if st.button("Ufff, mejor no..."):
            st.rerun()

def add_saga_popover():
    nom_saga = st.text_input("Nombre de la saga")
    if st.button("Guardar", icon="💾"):
        saga_service.create(nom_saga)

# ==========================================================================================================

st.set_page_config(
    page_title="Editar libro"
)

st.write("# ✏️ Editar libro")

libro = libro_service.get_libro(st.session_state["info_libro_id"])

if libro.url_portada:
    col01, col02 = st.columns([2.5, 7.5])
    with col01:
        st.image(libro.url_portada)
    with col02:
        titulo = st.text_input("Título", libro.titulo, disabled=not st.session_state["editando_libro"])
        id_saga = select_saga(libro.id_saga)
        isbn = st.text_input("ISBN", libro.isbn, disabled=not st.session_state["editando_libro"])
else: 
    titulo = st.text_input("Título", libro.titulo, disabled=not st.session_state["editando_libro"])
    id_saga = select_saga(libro.id_saga)
    isbn = st.text_input("ISBN", libro.isbn, disabled=not st.session_state["editando_libro"])

col11, col12, col13 = st.columns(3)
col21, col22, col23 = st.columns(3)
with col11:
    editorial = st.text_input("Editorial", libro.editorial, disabled=not st.session_state["editando_libro"])
with col12:
    num_pag = st.text_input("Número de páginas", libro.num_pag if libro.num_pag else None, disabled=not st.session_state["editando_libro"])
with col13:
    idioma = select_idioma()
with col21:
    fecha_public = select_date("Fecha de publicación", libro.fecha_public)
with col22:
    en_wishlist = select_wishlist(libro.en_wishlist)
with col23:
    prioridad_wishlist = select_prioridad_wishlist(libro.prioridad_wishlist)

generos = ",".join(select_genero(libro.genero))

url_portada = st.text_input("Portada", libro.url_portada, disabled=not st.session_state["editando_libro"])

sinopsis = add_texto("Sinopsis", libro.sinopsis)


with st.container(horizontal=True, horizontal_alignment="right"):
    if st.session_state["editando_libro"]:
        if st.button("Guardar", icon="💾"):
            libro_service.update(
                id_libro=libro.id_libro,
                id_saga=id_saga,
                titulo=titulo,
                isbn=isbn,
                num_pag=int(num_pag) if num_pag else None,
                genero=generos,
                idioma=idioma,
                sinopsis=sinopsis,
                fecha_public=fecha_public,
                url_portada=url_portada,
                editorial=editorial,
                en_wishlist=en_wishlist,
                prioridad_wishlist=prioridad_wishlist
            )
            st.session_state["editando_libro"] = False
            st.session_state["libro_editado"] = True
            st.switch_page("./pages/biblioteca.py")
    else:
        if st.button("", icon=":material/edit:"):
                st.session_state["editando_libro"] = True
                st.rerun()

        if st.button("", icon=":material/delete:"):
            confirm_delete(libro.id_libro)