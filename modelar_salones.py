import streamlit as st
import pandas as pd
import os

def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

def save_data(salones, file_path):
    salones.to_csv(file_path, index=False)

def app():
    st.title("Modelar Salones - UPCH")

    uploaded_file = st.file_uploader("Cargar archivo CSV de salones", type=['csv'])
    if uploaded_file is not None:
        salones = pd.read_csv(uploaded_file)
    else:
        salones = pd.DataFrame()

    st.write("## Salones Disponibles")
    st.write(salones)
    
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

    st.write("## Salones Actualizados")
    st.write(salones)

    with st.form(key='delete_salon'):
        st.write("### Eliminar Salón")
        salon_to_delete = st.selectbox("Selecciona un salón para eliminar", salones['salon'] if 'salon' in salones else [])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            salones = salones[salones['salon'] != salon_to_delete]
            st.success(f"Salón {salon_to_delete} eliminado exitosamente")

    st.markdown("## Descargar CSV Actualizado")
    st.markdown("Haz clic abajo para descargar el archivo CSV actualizado.")
    st.download_button(
        label="Descargar CSV",
        data=salones.to_csv(index=False),
        file_name='salones_actualizados.csv',
        mime='text/csv'
    )

    save_data(salones, 'salones.csv')

if __name__ == '__main__':
    app()

