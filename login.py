import streamlit as st
from PIL import Image

def app():
    # Cargar la imagen de la insignia de la universidad
    university_logo = Image.open("Logo_upch.png")

    # Credenciales de inicio de sesión
    User = "41650931"
    Password = "cayetano"

    # Estilo CSS para el formulario de inicio de sesión
    login_form_style = """
        <style>
        .login-form {
            background-color: black;
            padding: 20px;
            border-radius: 10px;
            color: white;
        }
        .login-form input[type="text"], 
        .login-form input[type="password"] {
            background-color: #333333;
            color: white;
            border: none;
            padding: 8px;
            margin-bottom: 10px;
            border-radius: 5px;
            width: 100%;
        }
        .login-form input[type="submit"] {
            background-color: #1f77b4;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        </style>
    """

    # Mostrar estilo CSS para el formulario de inicio de sesión
    st.markdown(login_form_style, unsafe_allow_html=True)

    # Mostrar logo y título de la aplicación
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
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            st.write("""
            ## Bienvenido a la Plataforma de Gestión de Cursos de Ingeniería Informática - UPCH
            En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.
            """)
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    app()

