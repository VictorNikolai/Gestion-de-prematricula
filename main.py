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

User = "41650931"
Password = "cayetano"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

set_background()

if not st.session_state.logged_in:
    login(encoded_logo, User, Password)
else:
    app = MultiApp()

    app.add_app("Modelar Salones", modelar_salones_app)
    app.add_app("Modelar Ambientes", modelar_ambientes_app)
    app.add_app("Modelar Cursos", modelar_cursos_app)
    app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
    app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
    app.add_app("Optimización de Horarios", optimizar_horarios_app)

    selected_app = st.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

    for app in app.apps:
        if app['title'] == selected_app:
            app['function']()
            break
