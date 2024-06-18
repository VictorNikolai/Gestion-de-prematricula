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
            st.experimental_set_query_params(page="sobre_cayetano")
            st.write("Nuestros estudiantes eligen la Universidad Peruana Cayetano Heredia por muchas razones, entre las que resaltan la alta calidad académica. Además, eligen un perfil de profesores comprometidos con generar conocimiento valioso para impulsar el desarrollo, y el poder compartir con estudiantes muy determinados en sus objetivos y ansiosos por descubrir nuevas tendencias. Más allá de contar con los más altos estándares internacionales, académicos y de investigación, en Cayetano sentimos que tenemos un compromiso con la sociedad, y nos esforzamos juntos, investigadores, personal docente y estudiantes, para lograr un aporte significativo que genere bienestar en todos los campos en los que trabajamos.")

    with col2:
        if st.button("Admisión", key="admision_button"):
            st.experimental_set_query_params(page="admision")
            st.write("Contamos con la mejor selección de alumnos, investigadores, docentes que nos han llevado a ser considerados entre las mejores universidades del Perú. Si el aprendizaje continuo, la curiosidad por descubrir, y el ser parte de una comunidad de excelencia y prestigio. Elige el proceso que corresponde con tu perfil, y postula a Cayetano. Cuenta con nuestro compromiso de formarte como un profesional de primer nivel.")

    with col3:
        if st.button("Pregrado", key="pregrado_button"):
            st.experimental_set_query_params(page="pregrado")
            st.write("Información sobre programas de pregrado ofrecidos.")

    with col1:
        if st.button("Posgrado", key="posgrado_button"):
            st.experimental_set_query_params(page="posgrado")
            st.write("Información sobre programas de posgrado ofrecidos.")

    with col2:
        if st.button("Educación Continua", key="educacion_continua_button"):
            st.experimental_set_query_params(page="educacion_continua")
            st.write("Oferta de educación continua y cursos.")

    with col3:
        if st.button("Investigación", key="investigacion_button"):
            st.experimental_set_query_params(page="investigacion")
            st.write("Actividades de investigación y proyectos.")

    with col1:
        if st.button("Internacionalización", key="internacionalizacion_button"):
            st.experimental_set_query_params(page="internacionalizacion")
            st.write("Programas y actividades internacionales.")

    st.write("¡Explora y disfruta de la plataforma!")
