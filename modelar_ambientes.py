import streamlit as st
import pandas as pd
import os

def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        ambientes_data = {
            'Tipo de Ambiente': ['Laboratorio', 'Aula', 'Auditorio'],
            'Descripción': ['Equipado con computadoras', 'Salón de clases estándar', 'Espacio para eventos grandes']
        }
        return pd.DataFrame(ambientes_data)

def save_data(ambientes, file_path):
    ambientes.to_csv(file_path, index=False)

def app():
    st.title("Modelar Tipos de Ambientes - UPCH")

    uploaded_file = st.file_uploader("Cargar archivo CSV de ambientes", type=['csv'])
    if uploaded_file is not None:
        ambientes = pd.read_csv(uploaded_file)
    else:
        ambientes = pd.DataFrame()

    st.write("## Tipos de Ambientes Disponibles")
    st.write(ambientes)
    
    with st.form(key='add_ambiente'):
        st.write("### Añadir Nuevo Tipo de Ambiente")
        tipo = st.text_input("Tipo de Ambiente")
        descripcion = st.text_input("Descripción")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_ambiente = pd.DataFrame({'Tipo de Ambiente': [tipo], 'Descripción': [descripcion]})
            ambientes = pd.concat([ambientes, new_ambiente], ignore_index=True)
            save_data(ambientes, 'ambientes.csv')
            st.success(f"Tipo de Ambiente '{tipo}' añadido exitosamente")
            st.experimental_rerun()

    st.write("## Tipos de Ambientes Actualizados")
    st.write(ambientes)

    with st.form(key='delete_ambiente'):
        st.write("### Eliminar Tipo de Ambiente")
        ambiente_a_eliminar = st.selectbox("Selecciona el Tipo de Ambiente a eliminar", ambientes['Tipo de Ambiente'] if 'Tipo de Ambiente' in ambientes else [])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            ambientes = ambientes[ambientes['Tipo de Ambiente'] != ambiente_a_eliminar]
            save_data(ambientes, 'ambientes.csv')
            st.success(f"Tipo de Ambiente '{ambiente_a_eliminar}' eliminado exitosamente")
            st.experimental_rerun()

    st.markdown("## Descargar CSV Actualizado")
    st.markdown("Haz clic abajo para descargar el archivo CSV actualizado.")
    st.download_button(
        label="Descargar CSV",
        data=ambientes.to_csv(index=False),
        file_name='ambientes_actualizados.csv',
        mime='text/csv'
    )

if __name__ == '__main__':
    app()
