# main.py
import streamlit as st
from multiapp import MultiApp
from login import login, set_background
from home import app as home_app  # Importa tu aplicación home desde home.py
import os
import base64

st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

current_dir = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(current_dir, "logo_upch.png")

with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

User = "0000"  # Tu usuario
Password = "0000"  # Tu contraseña

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

set_background()

if not st.session_state.logged_in:
    login(encoded_logo, User, Password)
else:
    app = MultiApp()

    app.add_app("Home", home_app)  # Agrega la aplicación home
    app.add_app("Modelar Salones", modelar_salones_app)
    app.add_app("Modelar Ambientes", modelar_ambientes_app)
    app.add_app("Modelar Cursos", modelar_cursos_app)
    app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
    app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
    app.add_app("Optimización de Horarios", optimizar_horarios_app)

    selected_app = "Home"  # Selecciona automáticamente la aplicación home después del inicio de sesión

    for app_page in app.apps:
        if app_page['title'] == selected_app:
            app_page['function']()  # Ejecuta la aplicación home
            break
