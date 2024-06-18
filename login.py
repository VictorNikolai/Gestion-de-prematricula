import streamlit as st
from PIL import Image

def login(encoded_logo, User, Password):
    # Cargar el logo de la universidad
    university_logo = Image.open("logo_upch.png")

    # Establecer el fondo de pantalla
    set_background()

    # Centrar el contenido principal
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenedor principal centrado
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Mostrar el logo, título y subheader
    st.image(university_logo, width=200)
    st.title("🎓 Plataforma de Gestión de Cursos - UPCH")
    st.subheader("Inicio de Sesión")

    # Formulario de inicio de sesión
    with st.form(key="login_form", class_="login-form"):
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

    # Cerrar el contenedor principal centrado
    st.markdown('</div>', unsafe_allow_html=True)

def set_background():
    background_url = "https://360.cayetano.edu.pe/wp-content/uploads/sites/25/2024/03/53135168333_7b780465e9_k.jpg"
    page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100vh;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
