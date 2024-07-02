import streamlit as st
import pandas as pd
import os

# Función para cargar los datos desde un archivo CSV si existe, o crear datos iniciales si no existe el archivo
def load_data(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        st.warning(f'El archivo {filename} no existe.')
        return None

# Función para guardar los datos en un archivo CSV
def save_data(ambientes, filename):
    ambientes.to_csv(filename, index=False)

# Función principal de la aplicación
def app():
    st.title("Modelar Tipos de Ambientes - UPCH")

    # Componente para que el usuario suba un archivo CSV
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=['csv'])

    if uploaded_file is not None:
        ambientes = pd.read_csv(uploaded_file)
        st.write("## Tipos de Ambientes Cargados")
        st.write(ambientes)

        # Mostrar tipos de ambientes disponibles
        st.write("## Tipos de Ambientes Disponibles")
        st.write(ambientes)

        # Formulario para añadir un nuevo tipo de ambiente
        with st.form(key='add_ambiente'):
            st.write("### Añadir Nuevo Tipo de Ambiente")
            tipo = st.text_input("Tipo de Ambiente")
            descripcion = st.text_input("Descripción")
            submit = st.form_submit_button("Añadir")

            if submit:
                new_ambiente = pd.DataFrame({'Tipo de Ambiente': [tipo], 'Descripción': [descripcion]})
                ambientes = pd.concat([ambientes, new_ambiente], ignore_index=True)
                save_data(ambientes, uploaded_file.name)
                st.success(f"Tipo de Ambiente '{tipo}' añadido exitosamente")
                st.experimental_rerun()

        # Formulario para eliminar un tipo de ambiente
        with st.form(key='delete_ambiente'):
            st.write("### Eliminar Tipo de Ambiente")
            ambiente_a_eliminar = st.selectbox("Selecciona el Tipo de Ambiente a eliminar", ambientes['Tipo de Ambiente'])
            submit_delete = st.form_submit_button("Eliminar")

            if submit_delete:
                ambientes = ambientes[ambientes['Tipo de Ambiente'] != ambiente_a_eliminar]
                save_data(ambientes, uploaded_file.name)
                st.success(f"Tipo de Ambiente '{ambiente_a_eliminar}' eliminado exitosamente")
                st.experimental_rerun()

        # Mostrar los tipos de ambientes actualizados
        st.write("## Tipos de Ambientes Actualizados")
        st.write(ambientes)

# Estilo CSS para centrar el contenido
st.markdown(
    """
    <style>
    .stApp {
        max-width: 1200px;
        margin: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextArea, .stTextInput, .stNumberInput, .stSelectbox, .stButton {
        width: 100%;
        max-width: 600px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == '__main__':
    app()
