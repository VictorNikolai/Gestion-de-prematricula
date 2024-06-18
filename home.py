# home.py
import streamlit as st

def app():
    st.title("Bienvenido a la Página de Inicio")
    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.header("Selecciona una sección para comenzar:")

    # Botones estilizados para cada funcionalidad
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Modelar Salones", key="modelar_salones_button"):
            st.experimental_set_query_params(page="modelar_salones")
    
    with col2:
        if st.button("Modelar Ambientes", key="modelar_ambientes_button"):
            st.experimental_set_query_params(page="modelar_ambientes")
    
    with col3:
        if st.button("Modelar Cursos", key="modelar_cursos_button"):
            st.experimental_set_query_params(page="modelar_cursos")
    
    with col1:
        if st.button("Requerimiento de Ambientes", key="requerimiento_ambientes_button"):
            st.experimental_set_query_params(page="requerimiento_ambientes")
    
    with col2:
        if st.button("Asignación de Alumnos", key="asignacion_alumnos_button"):
            st.experimental_set_query_params(page="asignacion_alumnos")
    
    with col3:
        if st.button("Optimización de Horarios", key="optimizar_horarios_button"):
            st.experimental_set_query_params(page="optimizar_horarios")

    st.write("¡Explora y disfruta de la plataforma!")
