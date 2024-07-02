import streamlit as st
from PIL import Image
import base64

def login(encoded_logo, User, Password):
    university_logo = Image.open("logo_upch.png")
    set_background()
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
        .form-container {
            max-width: 300px;
            margin: auto;
            padding: 20px;
            background-color: #f9f9f9; /* Fondo gris */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        """
        , unsafe_allow_html=True)

    st.markdown("<div class='logo-container'>"
                "<img src='data:image/png;base64,{}' class='img-fluid' width='200'>"
                "</div>".format(encoded_logo), unsafe_allow_html=True)

    st.markdown("<div class='title-container'><h1>🎓 Plataforma de Gestión de Cursos - UPCH</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader-container'><h3>Inicio de Sesión</h3></div>", unsafe_allow_html=True)

    with st.form(key="login_form"):
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        username = st.text_input("Usuario:", value="", key="username")
        password = st.text_input("Contraseña:", type="password", value="", key="password")
        submit = st.form_submit_button("Iniciar Sesión")

        if submit:
            if username == User and password == Password:
                st.session_state.logged_in = True
                st.success("¡Inicio de sesión exitoso!")
                st.balloons()
                st.experimental_rerun()
            else:
                st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

        st.markdown("</div>", unsafe_allow_html=True)  # Cerrar el contenedor form-container

def set_background():
    background_url = "https://raw.githubusercontent.com/VictorNikolai/Gestion-de-prematricula/main/cayetano.png"
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

# Llamar a la función principal para ejecutar la aplicación
login("encoded_logo_here", "tu_usuario", "tu_contraseña")
