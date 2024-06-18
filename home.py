# home.py
import streamlit as st

def app():
    st.title("Bienvenido a la Página de Inicio")
    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")
    
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Descubre nuestras áreas principales:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Sobre Cayetano", key="sobre_cayetano_button"):
            st.write("Información detallada sobre la Universidad Cayetano Heredia.")
            st.experimental_set_query_params(page="sobre_cayetano")

    with col2:
        if st.button("Admisión", key="admision_button"):
            st.write("Proceso de admisión para nuevos estudiantes.")
            st.experimental_set_query_params(page="admision")

    with col3:
        if st.button("Pregrado", key="pregrado_button"):
            st.write("Información sobre programas de pregrado ofrecidos.")
            st.experimental_set_query_params(page="pregrado")

    with col1:
        if st.button("Posgrado", key="posgrado_button"):
            st.write("Información sobre programas de posgrado ofrecidos.")
            st.experimental_set_query_params(page="posgrado")

    with col2:
        if st.button("Educación Continua", key="educacion_continua_button"):
            st.write("Oferta de educación continua y cursos.")
            st.experimental_set_query_params(page="educacion_continua")

    with col3:
        if st.button("Investigación", key="investigacion_button"):
            st.write("Actividades de investigación y proyectos.")
            st.experimental_set_query_params(page="investigacion")

    with col1:
        if st.button("Internacionalización", key="internacionalizacion_button"):
            st.write("Programas y actividades internacionales.")
            st.experimental_set_query_params(page="internacionalizacion")

    st.write("¡Explora y disfruta de la plataforma!")

