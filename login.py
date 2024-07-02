import streamlit as st
from PIL import Image
import base64

def login(encoded_logo, User, Password):
    university_logo = Image.open("logo_upch.png")
    set_background()
    st.markdown(
        """
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url('https://raw.githubusercontent.com/VictorNikolai/Gestion-de-prematricula/main/cayetano.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }
        .form-container {
            max-width: 300px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-container .stTextInput {
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 8px;
            width: 100%;
            margin-bottom: 10px;
            box-sizing: border-box;
        }
        .form-container .stButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-top: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .form-container .stButton:hover {
            background-color: #45a049;
        }
        </style>
        """
        , unsafe_allow_html=True)

    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    
    st.image(university_logo, width=200)
    st.markdown("<h1 style='text-align:center;'>🎓 Plataforma de Gestión de Cursos - UPCH</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Inicio de Sesión</h3>", unsafe_allow_html=True)

    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="", key="username", class_="stTextInput")
        password = st.text_input("Contraseña:", type="password", value="", key="password", class_="stTextInput")
        submit = st.form_submit_button("Iniciar Sesión", class_="stButton")

        if submit:
            if username == User and password == Password:
                st.session_state.logged_in = True
                st.success("¡Inicio de sesión exitoso!")
                st.balloons()
                st.experimental_rerun()
            else:
                st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

    st.markdown("</div>", unsafe_allow_html=True)  # Cerrar el contenedor form-container
    st.markdown("</div>", unsafe_allow_html=True)  # Cerrar el contenedor login-container

def set_background():
    pass  # Mantenemos la función set_background como está, ya que no la estamos utilizando actualmente.

# Llamar a la función principal para ejecutar la aplicación
login("encoded_logo_here", "tu_usuario", "tu_contraseña")

