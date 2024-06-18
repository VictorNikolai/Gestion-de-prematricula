import streamlit as st

def app():
    st.title("Bienvenido a la Página de Inicio")
    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }
        .button-container {
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Selecciona una sección para comenzar:")

    with st.markdown("<div class='centered'>", unsafe_allow_html=True):
        with st.markdown("<div class='button-container'>", unsafe_allow_html=True):
            if st.button("Sobre Cayetano"):
                st.query_params["page"] = "sobre_cayetano"
                st.write("Información sobre la historia y misión de la Universidad.")
        
        with st.markdown("<div class='button-container'>", unsafe_allow_html=True):
            if st.button("Admisión"):
                st.query_params["page"] = "admision"
                st.write("Requisitos y procedimientos para el proceso de admisión.")
        
        with st.markdown("<div class='button-container'>", unsafe_allow_html=True):
            if st.button("Teléfonos de Docentes"):
                st.query_params["page"] = "telefonos_docentes"
                st.write("Lista de números de teléfono para contactar a los docentes.")
        
        with st.markdown("<div class='button-container'>", unsafe_allow_html=True):
            if st.button("Teléfonos de Ayuda"):
                st.query_params["page"] = "telefonos_ayuda"
                st.write("Números de contacto para recibir ayuda y soporte técnico.")
        
        with st.markdown("<div class='button-container'>", unsafe_allow_html=True):
            if st.button("Teléfonos de Administración"):
                st.query_params["page"] = "telefonos_administracion"
                st.write("Contactos principales del departamento de administración.")

    st.write("¡Explora y disfruta de la plataforma!")

