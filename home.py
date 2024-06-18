# home.py
import streamlit as st

def app():
    st.title("Bienvenido a la Página de Inicio")
    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.header("Descubre nuestras áreas principales:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Sobre Cayetano", key="sobre_cayetano_button"):
            st.experimental_set_query_params(page="sobre_cayetano")
    
    with col2:
        if st.button("Admisión", key="admision_button"):
            st.experimental_set_query_params(page="admision")
    
    with col3:
        if st.button("Pregrado", key="pregrado_button"):
            st.experimental_set_query_params(page="pregrado")
    
    with col1:
        if st.button("Posgrado", key="posgrado_button"):
            st.experimental_set_query_params(page="posgrado")
    
    with col2:
        if st.button("Educación Continua", key="educacion_continua_button"):
            st.experimental_set_query_params(page="educacion_continua")
    
    with col3:
        if st.button("Investigación", key="investigacion_button"):
            st.experimental_set_query_params(page="investigacion")
    
    with col1:
        if st.button("Internacionalización", key="internacionalizacion_button"):
            st.experimental_set_query_params(page="internacionalizacion")

    st.write("¡Explora y disfruta de la plataforma!")
