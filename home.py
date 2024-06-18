# home.py
import streamlit as st
from asignacion_alumnos import app as asignacion_alumnos_app
from modelar_salones import app as modelar_salones_app
# Importar otras aplicaciones según sea necesario

def app():
    st.title("Página Principal - Plataforma de Gestión de Cursos")
    
    # Leer los parámetros de consulta
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["home"])[0]

    if page == "home":
        # Barra de navegación para seleccionar la sección
        selected_app = st.selectbox("Selecciona una sección", 
                                    ["Asignación de Alumnos", "Modelar Salones"])  # Agrega más opciones según sea necesario
        
        # Renderizar la aplicación seleccionada
        if selected_app == "Asignación de Alumnos":
            asignacion_alumnos_app()
        elif selected_app == "Modelar Salones":
            modelar_salones_app()
        # Añadir más condiciones para otras secciones

# Ejecutar la aplicación principal
if __name__ == "__main__":
    app()
