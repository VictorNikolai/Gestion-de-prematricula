# home.py
import streamlit as st
from asignacion_alumnos import app as asignacion_alumnos_app
from modelar_salones import app as modelar_salones_app
# Import other apps here as needed

def app():
    st.title("Página Principal - Plataforma de Gestión de Cursos")
    
    # Retrieve query parameters
    query_params = st.query_params()
    page = query_params.get("page", "home")  # Default to "home" page if no page specified

    # Barra de navegación para seleccionar la sección
    selected_app = st.selectbox("Selecciona una sección", 
                                ["Asignación de Alumnos", "Modelar Salones"])  # Add more options as needed

    # Execute the selected application
    if selected_app == "Asignación de Alumnos":
        asignacion_alumnos_app()
    elif selected_app == "Modelar Salones":
        modelar_salones_app()
    # Add more conditions for other sections

# Main app execution
if __name__ == "__main__":
    app()
