import streamlit as st
from multiapp import MultiApp
from modelar_salones import app as modelar_salones_app
from modelar_ambientes import app as modelar_ambientes_app
from modelar_cursos import app as modelar_cursos_app
from requerimiento_ambientes import app as requerimiento_ambientes_app
from asignacion_alumnos import app as asignacion_alumnos_app
from optimizar_horarios import app as optimizar_horarios_app
from PIL import Image

# Definir la imagen de fondo
university_background = "https://raw.githubusercontent.com/VictorNikolai/Gestion-de-prematricula/main/universidad.jpg"

# Estilo de fondo
background_style = f"""
    <style>
    body {{
        background-image: url('{university_background}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp {{
        background-color: rgba(255, 255, 255, 0.9);  /* Fondo semi-transparente para mejor legibilidad */
        padding: 1rem;
        min-height: 100vh;  /* Ajustar al tamaño de la ventana */
    }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# Configurar el diseño de la página sin icono
st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH", page_icon=":mortar_board:")

# Ruta al logo (ajusta según tu estructura de directorios)
logo_path = "logo_upch.png"

# Cargar el logo y convertir a base64
try:
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
except FileNotFoundError:
    st.warning("No se encontró el archivo del logo.")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

# Variable de estado para verificar si el usuario ha iniciado sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Función de inicio de sesión
def login():
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/png;base64,{encoded_logo}" alt="Logo UPCH" width="100">
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

    # Crear una barra de navegación en la parte superior
    selected_app = st.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

    # Ejecutar la aplicación seleccionada
    for app in app.apps:
        if app['title'] == selected_app:
            app['function']()
            break
