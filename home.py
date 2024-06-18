import streamlit as st

def main():
    st.title("Mi Aplicación con Streamlit")

    # Lee los parámetros de consulta
    page = st.query_params.get("page", "home")

    if page == "home":
        st.header("Bienvenido a la Página de Inicio")
        st.write("Esta es la página principal de la aplicación.")

        if st.button("Ir a la página de detalles"):
            st.query_params["page"] = "details"

    elif page == "details":
        st.header("Detalles de la Página")
        st.write("Estos son los detalles de la página seleccionada.")

        if st.button("Volver a la página de inicio"):
            st.query_params["page"] = "home"

    # Enlaces de navegación
    st.write("Navega usando los enlaces:")
    if st.button("Ir a la página de inicio"):
        st.query_params["page"] = "home"
    if st.button("Ir a la página de detalles"):
        st.query_params["page"] = "details"

if __name__ == "__main__":
    main()

