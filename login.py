import streamlit as st
from PIL import Image
import base64

def get_base64(png_file):
    with open(png_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def app():
    # Llamar a set_background con la imagen deseada
    set_background("universidad.png")  # Asegúrate de que "universidad.png" esté en el mismo directorio

    st.title("🎓 Plataforma de Gestión de Cursos - UPCH")
    st.subheader("Inicio de Sesión")

    User = "41650931"
    Password = "cayetano"

    with st.form(key="login_form"):
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        if username == User and password == Password:
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
