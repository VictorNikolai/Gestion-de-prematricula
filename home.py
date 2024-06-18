# home.py
import streamlit as st

def app():
    st.title("Bienvenido a la Página de Inicio")
    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.header("Selecciona una sección para comenzar:")

    # Botones para cada funcionalidad
    if st.button("Modelar Salones"):
        st.query_params["page"] = "modelar_salones"
    if st.button("Modelar Ambientes"):
        st.query_params["page"] = "modelar_ambientes"
    if st.button("Modelar Cursos"):
        st.query_params["page"] = "modelar_cursos"
    if st.button("Requerimiento de Ambientes"):
        st.query_params["page"] = "requerimiento_ambientes"
    if st.button("Asignación de Alumnos"):
        st.query_params["page"] = "asignacion_alumnos"
    if st.button("Optimización de Horarios"):
        st.query_params["page"] = "optimizar_horarios"

    st.write("¡Explora y disfruta de la plataforma!")

