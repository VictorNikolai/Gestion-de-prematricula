import streamlit as st

def app():
    # Configuración de la página
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    # Contenido de la aplicación
    st.markdown(
        """
        <style>
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            height: 100vh;  /* Ajusta la altura al 100% del viewport */
            margin-top: -50px;  /* Ajusta el margen superior para centrar mejor */
        }
        .centered-text {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='centered-title'>Bienvenido a la Página de Inicio</h1>", unsafe_allow_html=True)

    st.markdown("<p class='centered-text'>Aquí puedes comenzar a explorar las funcionalidades de la plataforma.</p>", unsafe_allow_html=True)

    st.header("Selecciona una sección para comenzar:")

    if st.button("Sobre Cayetano", key="sobre_cayetano"):
        st.query_params["page"] = "sobre_cayetano"
        st.write("Información sobre la historia y misión de la Universidad.")
    if st.button("Admisión", key="admision"):
        st.query_params["page"] = "admision"
        st.write("Requisitos y procedimientos para el proceso de admisión.")
    if st.button("Teléfonos de Docentes", key="telefonos_docentes"):
        st.query_params["page"] = "telefonos_docentes"
        st.write("Lista de números de teléfono para contactar a los docentes.")
    if st.button("Teléfonos de Ayuda", key="telefonos_ayuda"):
        st.query_params["page"] = "telefonos_ayuda"
        st.write("Números de contacto para recibir ayuda y soporte técnico.")
    if st.button("Teléfonos de Administración", key="telefonos_administracion"):
        st.query_params["page"] = "telefonos_administracion"
        st.write("Contactos principales del departamento de administración.")

    st.markdown("<p class='centered-text'>¡Explora y disfruta de la plataforma!</p>", unsafe_allow_html=True)

def main():
    app()

if __name__ == "__main__":
    main()
