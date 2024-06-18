import streamlit as st
from PIL import Image

def app():
    # URL de la imagen de fondo en GitHub
    university_background_url = "https://raw.githubusercontent.com/VictorNikolai/Gestion-de-prematricula/main/universidad.jpg"

    # Cargar la imagen de fondo desde la URL
    university_background = Image.open(urllib.request.urlopen(university_background_url))

    # Establecer el estilo CSS para el fondo de pantalla
    background_style = f"""
        <style>
        .stApp {{
            background-image: url('{university_background_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

    # Contenido de la aplicación de inicio de sesión
    st.title("🎓 Plataforma de Gestión de Cursos - UPCH")
    st.subheader("Inicio de Sesión")

    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        # Validación de usuario y contraseña (simulada)
        if username == "41650931" and password == "cayetano":
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            st.write("""
                ## Bienvenido a la Plataforma de Gestión de Cursos - UPCH
                En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.
            """)
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    app()
