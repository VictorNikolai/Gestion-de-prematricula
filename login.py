import streamlit as st
from PIL import Image

def app():
    # Cargar la imagen de la insignia de la universidad
    university_logo = Image.open("Logo_upch.png")

    # Credenciales de inicio de sesión
    User = "41650931"
    Password = "cayetano"

    # Crear el diseño del formulario de inicio de sesión con fondo negro
    st.image(university_logo, width=200)
    st.title("🎓 Plataforma de Gestión de Cursos - UPCH")
    st.subheader("Inicio de Sesión")

    # Estilo CSS para el formulario
    login_form_style = """
        <style>
        .login-form {
            background-color: black;
            padding: 20px;
            border-radius: 10px;
        }
        .stTextInput, .stTextArea {
            background-color: #f0f0f5;
            color: black;
        }
        </style>
    """
    st.markdown(login_form_style, unsafe_allow_html=True)

    with st.form(key="login_form", class_="login-form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        if username == User and password == Password:
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            st.write("""
            ## Bienvenido a la Plataforma de Gestión de Cursos de Ingeniería Informática - UPCH
            En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.
            """)
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    else:
        st.warning("Por favor, inicie sesión para continuar.")

if __name__ == "__main__":
    app()
