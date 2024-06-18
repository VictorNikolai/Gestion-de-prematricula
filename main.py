# main.py
import streamlit as st
from multiapp import MultiApp
from login import login, set_background
from modelar_salones import app as modelar_salones_app
from modelar_ambientes import app as modelar_ambientes_app
from modelar_cursos import app as modelar_cursos_app
from requerimiento_ambientes import app as requerimiento_ambientes_app
from asignacion_alumnos import app as asignacion_alumnos_app
from optimizar_horarios import app as optimizar_horarios_app
import os
import base64

st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

current_dir = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(current_dir, "logo_upch.png")

with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# Credenciales de inicio de sesión (simuladas para el ejemplo)
User = "41650931"
Password = "cayetano"

# Variable de estado para verificar si el usuario ha iniciado sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Función para establecer el fondo de pantalla globalmente
set_background()

# Mostrar la página de inicio de sesión si el usuario no ha iniciado sesión
if not st.session_state.logged_in:
    login(encoded_logo, User, Password)
else:
    # Crear una instancia de la aplicación múltiple
    app = MultiApp()

    # Agregar todas las aplicaciones
    app.add_app("Modelar Salones", modelar_salones_app)
    app.add_app("Modelar Ambientes", modelar_ambientes_app)
    app.add_app("Modelar Cursos", modelar_cursos_app)
    app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
    app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
    app.add_app("Optimización de Horarios", optimizar_horarios_app)

    # Crear una barra de navegación en la parte superior
    selected_app = st.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

    # Ejecutar la aplicación seleccionada
    for app in app.apps:
        if app['title'] == selected_app:
            app['function']()
            break
