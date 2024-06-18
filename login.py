# login.py
import streamlit as st
from PIL import Image
import base64

def login(encoded_logo, User, Password):
    # Cargar la imagen de la insignia de la universidad
    university_logo = Image.open("logo_upch.png")

    # Establecer el fondo de pantalla
    set_background()

    # Mostrar logo y título de la aplicación centrados
    st.markdown(
        """
        <style>
        .logo-container {
            display: flex;
            justify-content: center;
        }
        .title-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .subheader-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        </style>
        """
        , unsafe_allow_html=True)

    st.markdown("<div class='logo-container'>"
                "<img src='data:image/png;base64,{}' class='img-fluid' width='200'>"
                "</div>".format(encoded_logo), unsafe_allow_html=True)

    st.markdown("<div class='title-container'><h1>🎓 Plataforma de Gestión de Cursos - UPCH</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader-container'><h3>Inicio de Sesión</h3></div>", unsafe_allow_html=True)

    # Formulario de inicio de sesión
    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    # Procesamiento del formulario
    if submit:
        if username == User and password == Password:
            st.session_state.logged_in = True
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            # Redirigir a la página de inicio (home)
            st.experimental_set_query_params(page="home")
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

# Función para establecer el fondo de pantalla globalmente
def set_background():
    background_url = "https://raw.githubusercontent.com/VictorNikolai/Gestion-de-prematricula/06d35da9e3a46b3e4c80297a13c319f0097ce5ac/cayetano.png"
    page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Ajusta según tus necesidades */
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
