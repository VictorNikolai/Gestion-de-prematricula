import streamlit as st
import pandas as pd
import os

# Función para cargar los datos desde un archivo CSV o crear datos ficticios si no existe el archivo
def load_data():
    if os.path.exists('salones.csv'):
        return pd.read_csv('salones.csv')
    else:
        # Datos ficticios de salones para usar si no existe el archivo CSV
        salones_data = {
            'salon': ['A101', 'B202', 'C303', 'D404'],
            'capacidad': [30, 40, 50, 35],
            'ubicacion': ['Edificio A', 'Edificio B', 'Edificio C', 'Edificio D']
        }
        return pd.DataFrame(salones_data)

# Función para guardar los datos actualizados en un archivo CSV
def save_data(salones):
    salones.to_csv('salones.csv', index=False)

# Función principal que define la aplicación de Streamlit
def app():
    st.title("Modelar Salones - UPCH")

    # Cargar datos de salones
    salones = load_data()

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
            save_data(salones)
            st.success(f"Salón {salon} añadido exitosamente")
            st.experimental_rerun()

    # Mostrar los salones actualizados
    st.write("## Salones Actualizados")
    st.write(salones)

    # Permitir eliminar salones
    with st.form(key='delete_salon'):
        st.write("### Eliminar Salón")
        salon_to_delete = st.selectbox("Selecciona un salón para eliminar", salones['salon'])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            salones = salones[salones['salon'] != salon_to_delete]
            save_data(salones)
            st.success(f"Salón {salon_to_delete} eliminado exitosamente")
            st.experimental_rerun()

    # Agregar un botón para descargar el CSV actualizado
    st.markdown("## Descargar CSV Actualizado")
    st.markdown("Haz clic abajo para descargar el archivo CSV actualizado.")
    st.download_button(
        label="Descargar CSV",
        data=salones.to_csv(index=False),
        file_name='salones_actualizados.csv',
        mime='text/csv'
    )

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app()

