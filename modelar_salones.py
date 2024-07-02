import streamlit as st
import pandas as pd
import os

# Función para cargar los datos de los salones desde un archivo CSV o crear datos iniciales si no existe el archivo
def load_data(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        salones_data = {
            'Salón': ['A101', 'B202', 'C303', 'D404'],
            'Capacidad': [30, 40, 50, 35],
            'Ubicación': ['Edificio A', 'Edificio B', 'Edificio C', 'Edificio D']
        }
        return pd.DataFrame(salones_data)

# Función para guardar los datos de los salones en un archivo CSV
def save_data(salones, filename):
    salones.to_csv(filename, index=False)

# Función principal de la aplicación
def app():
    # Título principal de la aplicación
    st.title("Modelar Salones - UPCH")

    # Opción para cargar un archivo CSV existente o crear uno nuevo
    st.header("Cargar Archivo CSV")
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=['csv'])
    if uploaded_file is not None:
        filename = uploaded_file.name
        salones = pd.read_csv(uploaded_file)
    else:
        filename = 'salones.csv'
        salones = load_data(filename)

    # Mostrar los salones actuales
    st.write("## Salones Actuales")
    st.write(salones)

    # Sección para añadir un nuevo salón
    st.header("Añadir Nuevo Salón")
    with st.form(key='add_salon'):
        salon = st.text_input("Salón")
        capacidad = st.number_input("Capacidad", min_value=1)
        ubicacion = st.text_input("Ubicación")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_salon = pd.DataFrame({'Salón': [salon], 'Capacidad': [capacidad], 'Ubicación': [ubicacion]})
            salones = pd.concat([salones, new_salon], ignore_index=True)
            save_data(salones, filename)
            st.success(f"Salón {salon} añadido exitosamente")
            st.experimental_rerun()

    # Sección para eliminar un salón existente
    st.header("Eliminar Salón")
    with st.form(key='delete_salon'):
        salon_to_delete = st.selectbox("Selecciona un salón para eliminar", salones['Salón'])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            salones = salones[salones['Salón'] != salon_to_delete]
            save_data(salones, filename)
            st.success(f"Salón {salon_to_delete} eliminado exitosamente")
            st.experimental_rerun()

    # Mostrar la lista actualizada de salones
    st.header("Salones Actualizados")
    st.write(salones)

# Ejecutar la aplicación si este archivo es el punto de entrada principal
if __name__ == '__main__':
    app()

