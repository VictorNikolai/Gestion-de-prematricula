import streamlit as st
from PIL import Image

def login(encoded_logo, User, Password):
    university_logo = Image.open("logo_upch.png")

    # Centrar título y logo
    st.image(university_logo, width=200, caption='', use_column_width=True, align='center')
    st.title("🎓 Plataforma de Gestión de Cursos - UPCH", align='center')
    st.subheader("Inicio de Sesión", align='center')

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

