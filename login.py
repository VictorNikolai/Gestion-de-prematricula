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
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<div class='logo-container'>"
                "<img src='data:image/png;base64,{}' class='img-fluid' width='200'>"
                "</div>".format(encoded_logo), unsafe_allow_html=True)

    st.markdown("<div class='title-container'><h1>🎓 𝙿𝙻𝙰𝚃𝙰𝙵𝙾𝚁𝙼𝙰 𝙳𝙴 𝙶𝙴𝚂𝚃𝙸𝙾́𝙽 𝙳𝙴 𝙲𝚄𝚁𝚂𝙾𝚂 - 𝚄𝙿𝙲𝙷</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader-container'><h3>Inicio de Sesión</h3></div>", unsafe_allow_html=True)

    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        if username == User and password == Password:
            st.session_state.logged_in = True
            st.success("¡Inicio de sesión exitoso!")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

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
