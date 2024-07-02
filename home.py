import streamlit as st

def app():
    st.markdown(
        """
        <style>
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            height: 100vh;
            margin-top: -50px;
        }
        .horizontal-buttons {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='centered-title'>Bienvenido a la Página de Inicio</h1>", unsafe_allow_html=True)

    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.header("Selecciona una sección para comenzar:")

    # Contenedor para los botones horizontales
    with st.markdown("<div class='horizontal-buttons'>", unsafe_allow_html=True):
        if st.button("Sobre Cayetano"):
            st.query_params["page"] = "sobre_cayetano"
            st.write("Información sobre la historia y misión de la Universidad.")
        if st.button("Admisión"):
            st.query_params["page"] = "admision"
            st.write("Requisitos y procedimientos para el proceso de admisión.")
        if st.button("Teléfonos de Docentes"):
            st.query_params["page"] = "telefonos_docentes"
            st.write("Lista de números de teléfono para contactar a los docentes.")
        if st.button("Teléfonos de Ayuda"):
            st.query_params["page"] = "telefonos_ayuda"
            st.write("Números de contacto para recibir ayuda y soporte técnico.")
        if st.button("Teléfonos de Administración"):
            st.query_params["page"] = "telefonos_administracion"
            st.write("Contactos principales del departamento de administración.")

    st.write("¡Explora y disfruta de la plataforma!")

app()
