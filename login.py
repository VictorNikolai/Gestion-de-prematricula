# login.py
import streamlit as st
from PIL import Image
import base64

def login(encoded_logo, User, Password):
    # Cargar la imagen de la insignia de la universidad
    university_logo = Image.open("logo_upch.png")

    # Establecer el fondo de pantalla con efecto de desenfoque
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
        .blur-background {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url("{background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            filter: blur(8px); /* Aplica el efecto de desenfoque */
            z-index: -1; /* Coloca detrás de otros elementos */
        }
        </style>
        """
        , unsafe_allow_html=True)

    st.markdown("<div class='blur-background'></div>", unsafe_allow_html=True)  # Fondo desenfocado

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
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

# Función para establecer el fondo de pantalla globalmente
def set_background():
    background_url = "https://360.cayetano.edu.pe/wp-content/uploads/sites/25/2024/03/53135168333_7b780465e9_k.jpg"
    st.markdown(f"""
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
            position: relative;
        }}
        </style>
    """, unsafe_allow_html=True)

