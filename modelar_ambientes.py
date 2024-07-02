import streamlit as st
import pandas as pd
import os

# Función para cargar los datos desde un archivo CSV o crear datos ficticios si no existe el archivo
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        ambientes_data = {
            'Tipo de Ambiente': ['Laboratorio', 'Aula', 'Auditorio'],
            'Descripción': ['Equipado con computadoras', 'Salón de clases estándar', 'Espacio para eventos grandes']
        }
        return pd.DataFrame(ambientes_data)

# Función para guardar los datos actualizados en un archivo CSV
def save_data(ambientes, file_path):
    ambientes.to_csv(file_path, index=False)

# Función principal que define la aplicación de Streamlit
def app():
    st.title("Modelar Tipos de Ambientes - UPCH")

    # Cargar datos de tipos de ambientes desde un archivo CSV existente o crear datos ficticios si no existe
    ambientes = load_data('ambientes.csv')

    # Mostrar los tipos de ambientes disponibles
    st.write("## Tipos de Ambientes Disponibles")
    st.write(ambientes)
    
    # Permitir agregar nuevos tipos de ambientes
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

    # Mostrar los tipos de ambientes actualizados
    st.write("## Tipos de Ambientes Actualizados")
    st.write(ambientes)

    # Permitir eliminar tipos de ambientes
    with st.form(key='delete_ambiente'):
        st.write("### Eliminar Tipo de Ambiente")
        ambiente_a_eliminar = st.selectbox("Selecciona el Tipo de Ambiente a eliminar", ambientes['Tipo de Ambiente'] if 'Tipo de Ambiente' in ambientes else [])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            ambientes = ambientes[ambientes['Tipo de Ambiente'] != ambiente_a_eliminar]
            save_data(ambientes, 'ambientes.csv')
            st.success(f"Tipo de Ambiente '{ambiente_a_eliminar}' eliminado exitosamente")

    # Agregar un botón para descargar el CSV actualizado
    st.markdown("## Descargar CSV Actualizado")
    st.markdown("Haz clic abajo para descargar el archivo CSV actualizado.")
    st.download_button(
        label="Descargar CSV",
        data=ambientes.to_csv(index=False),
        file_name='ambientes_actualizados.csv',
        mime='text/csv'
    )

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app()
