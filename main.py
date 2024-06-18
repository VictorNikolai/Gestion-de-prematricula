import streamlit as st
from multiapp import MultiApp
from modelar_salones import app as modelar_salones_app
from modelar_ambientes import app as modelar_ambientes_app
from modelar_cursos import app as modelar_cursos_app
from requerimiento_ambientes import app as requerimiento_ambientes_app
from asignacion_alumnos import app as asignacion_alumnos_app
from optimizar_horarios import app as optimizar_horarios_app
import os
import base64
from PIL import Image

# Configurar el diseño de la página sin icono
st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al logo
logo_path = os.path.join(current_dir, "logo_upch.png")

# Cargar el logo y convertir a base64
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

# Credenciales de inicio de sesión (simuladas para el ejemplo)
User = "41650931"
Password = "cayetano"

# Inicialización de variables de sesión
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""

# Variable de estado para verificar si el usuario ha iniciado sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Función para establecer el fondo de pantalla globalmente
def set_background():
    background_url = "https://360.cayetano.edu.pe/wp-content/uploads/sites/25/2024/03/53135168333_7b780465e9_k.jpg"
    page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Llamar a la función para establecer el fondo de pantalla
set_background()

# Función de inicio de sesión
def login():
    # Estilo para el cuadro de inicio de sesión
    login_style = """
        <style>
        .login-container {
            background-color: black;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .login-container input[type="text"], .login-container input[type="password"] {
            background-color: #f5f5f5;
            border: none;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            width: 100%;
        }
        .login-container input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        </style>
    """
    st.markdown(login_style, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="login-container">
            <h2 style="color: white;">Inicio de Sesión</h2>
            <form id="login_form">
                <label style="color: white;">Usuario:</label>
                <input type="text" name="username" value="{st.session_state.username}">
                <br>
                <label style="color: white;">Contraseña:</label>
                <input type="password" name="password" value="{st.session_state.password}">
                <br>
                <input type="submit" value="Iniciar Sesión">
            </form>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.success("¡Inicio de sesión exitoso!")
        st.balloons()
        st.write("""
            ## Bienvenido a la Plataforma de Gestión de Cursos de Ingeniería Informática - UPCH
            En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.
        """)

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

    # Crear una barra de navegación en la parte superior
    selected_app = st.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

    # Ejecutar la aplicación seleccionada
    for app in app.apps:
        if app['title'] == selected_app:
            app['function']()
            break

