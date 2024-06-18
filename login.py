# login.py
import streamlit as st
from PIL import Image
import base64

def login(encoded_logo, User, Password):
    # Cargar la imagen de la insignia de la universidad
    university_logo = Image.open("logo_upch.png")

    # Establecer el fondo de pantalla
    set_background()

    # Centrar el logo y el título de la aplicación con color de texto negro
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            color: black; /* Cambia el color del texto a negro */
        }
        </style>
        """, unsafe_allow_html=True)

    with st.container():
        st.image(university_logo, width=200)
        st.title("🎓 Plataforma de Gestión de Cursos - UPCH")
        st.subheader("Inicio de Sesión")

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

