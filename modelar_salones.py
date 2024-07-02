import streamlit as st
import pandas as pd
import os

# Función para cargar los datos desde un archivo CSV o crear datos ficticios si no existe el archivo
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

# Función para guardar los datos actualizados en un archivo CSV
def save_data(salones, file_path):
    salones.to_csv(file_path, index=False)

# Función principal que define la aplicación de Streamlit
def app():
    st.title("Modelar Salones - UPCH")

    # Permitir al usuario cargar un archivo CSV desde su máquina
    uploaded_file = st.file_uploader("Cargar archivo CSV de salones", type=['csv'])
    if uploaded_file is not None:
        # Cargar los datos desde el archivo CSV subido por el usuario
        salones = pd.read_csv(uploaded_file)
    else:
        # Si no se ha cargado ningún archivo, inicializar con un DataFrame vacío
        salones = pd.DataFrame()

    # Mostrar los salones disponibles
    st.write("## Salones Disponibles")
    st.write(salones)
    
    # Permitir agregar nuevos salones
    with st.form(key='add_salon'):
        st.write("### Añadir Nuevo Salón")
        salon = st.text_input("Salón")
        capacidad = st.number_input("Capacidad", min_value=1)
        ubicacion = st.text_input("Ubicación")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_salon = pd.DataFrame({'salon': [salon], 'capacidad': [capacidad], 'ubicacion': [ubicacion]})
            salones = pd.concat([salones, new_salon], ignore_index=True)
            st.success(f"Salón {salon} añadido exitosamente")

    # Mostrar los salones actualizados
    st.write("## Salones Actualizados")
    st.write(salones)

    # Permitir eliminar salones
    with st.form(key='delete_salon'):
        st.write("### Eliminar Salón")
        salon_to_delete = st.selectbox("Selecciona un salón para eliminar", salones['salon'] if 'salon' in salones else [])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            salones = salones[salones['salon'] != salon_to_delete]
            st.success(f"Salón {salon_to_delete} eliminado exitosamente")

    # Agregar un botón para descargar el CSV actualizado
    st.markdown("## Descargar CSV Actualizado")
    st.markdown("Haz clic abajo para descargar el archivo CSV actualizado.")
    st.download_button(
        label="Descargar CSV",
        data=salones.to_csv(index=False),
        file_name='salones_actualizados.csv',
        mime='text/csv'
    )

    # Guardar los cambios en el archivo CSV
    save_data(salones, 'salones.csv')

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app()

