import streamlit as st
from multiapp import MultiApp
from modelar_salones import app as modelar_salones_app
from modelar_ambientes import app as modelar_ambientes_app
from modelar_cursos import app as modelar_cursos_app
from requerimiento_ambientes import app as requerimiento_ambientes_app
from asignacion_alumnos import app as asignacion_alumnos_app
from optimizar_horarios import app as optimizar_horarios_app
import pandas as pd
from PIL import Image
import os
import base64

# Configurar el diseño de la página sin icono
st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH", page_icon=":mortar_board:")

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al logo
logo_path = os.path.join(current_dir, "logo_upch.png")

# Cargar el logo y convertir a base64
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# Ruta al fondo de la universidad
university_background = os.path.join(current_dir, "universidad.jpg")

# Variable de estado para verificar si el usuario ha iniciado sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Función para cargar el estilo de fondo
def load_background_style():
    background_style = f"""
        <style>
        body {{
            background-image: url('file://{university_background}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .header-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
        }}
        .header-container img {{
            max-height: 100px;
            margin-right: 20px;
        }}
        .header-container h1 {{
            font-size: 2.5rem;
            margin: 0;
            color: white;  /* Color del texto */
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Función de inicio de sesión
def login():
    load_background_style()  # Cargar el estilo de fondo para la pantalla de inicio de sesión

    st.markdown(f"""
        <div class="header-container">
            <img src="data:image/png;base64,{encoded_logo}" alt="Logo UPCH">
            <h1>Plataforma de Gestión de Cursos - UPCH</h1>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Inicio de Sesión")

    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        if username == User and password == Password:
            st.session_state.logged_in = True
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

# Mostrar la página de inicio de sesión si el usuario no ha iniciado sesión
if not st.session_state.logged_in:
    login()
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

    load_background_style()  # Cargar el estilo de fondo para las otras secciones de la aplicación

    # Crear una barra de navegación en la parte superior
    selected_app = st.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

    # Ejecutar la aplicación seleccionada
    for app in app.apps:
        if app['title'] == selected_app:
            app['function']()

