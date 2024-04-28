import streamlit as st
import pandas as pd
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(layout="centered")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Crear el diseño del formulario de inicio de sesión
st.markdown(
    """
    <style>
    .stApp {
        background-color: #010a1c;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .portal-title {
        text-align: center;
        color: #fcfcfc;
        margin-bottom: 10px;
        font-size: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.image(university_logo, use_column_width=True)
st.markdown("<div class='login-container'><h3 class='portal-title'> 🎓 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢̄𝐜𝐮𝐥𝐚 - 𝐔𝐏𝐂𝐇 </h3>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input(" 𝚄𝚜𝚎𝚛: ", value=User)
    password = st.text_input("𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍:", type="password", value=Password)
    submit = st.form_submit_button("𝕃𝕠𝕘 𝕀𝕟")

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar los cursos si el inicio de sesión es correcto
if submit:
    if username == User and password == Password:
        st.success("¡Inicio de sesión exitoso!")

        # Bienvenida al estudiante con globos
        st.balloons()
        st.write("# ¡Bienvenido, Estudiante! 🎈🎉")

        # Descripción de la aplicación
        st.write("""
        ## Bienvenido a la Plataforma de Gestión de Cursos de Ingeniería Informática - UPCH

        En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.

        ¡Sumérgete en el mundo de la ingeniería informática y construye tu camino hacia el éxito académico!
        """)

        # Estilos CSS
        hide_table_row_index = """
                    <style>
                    tbody th {display:none;}
                    .blank {display:none;}
                    </style>
                    """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Función para obtener el color de fondo según el ciclo
        def get_bg_color(ciclo):
            colores = {
                "PRIMER": "#F0F8FF",   # Azul claro
                "SEGUNDO": "#E0FFFF",  # Turquesa claro
                "TERCER": "#FAFAD2",   # Amarillo claro
                "CUARTO": "#FAF0E6",   # Lino
                "QUINTO": "#FFF5EE",   # Seashell
                "SEXTO": "#F5F5DC",    # Beige
                "SEPTIMO": "#E6E6FA",  # Lavanda
                "OCTAVO": "#FFF0F5",   # Lavanda rojizo
                "NOVENO": "#F8F8FF",   # Azul fantasma
                "DECIMO": "#F5DEB3"    # Wheat
            }
            return colores.get(ciclo, "")  # Obtener el color correspondiente al ciclo o vacío si no hay coincidencia

        # Mostrar los cursos por ciclo con colores personalizados
        for ciclo in data["CICLO"].unique():
            cursos = data[data["CICLO"] == ciclo]
            st.subheader(f"{ciclo}")
            st.write(cursos.style.apply(lambda x: [f"background-color: {get_bg_color(ciclo)}"] * len(x), axis=1).to_html(escape=False), unsafe_allow_html=True)

        # Nota al pie
        st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

        # Mostrar la imagen del grafo de los cursos
        st.subheader("Grafo de los Cursos de Ingeniería Informática")
        st.write("En esta imagen se muestra un grafo que representa la estructura de los cursos de la carrera de Ingeniería Informática. Los nodos representan los cursos, y las conexiones entre ellos indican los prerrequisitos necesarios para llevar cada curso.")
        st.image("HITO 1 - GRUPO REZAGADOS.jpg", caption="Grafo de los Cursos de Ingeniería Informática")
    else:
        st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")












