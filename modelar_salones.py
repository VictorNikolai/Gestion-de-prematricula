import streamlit as st
import pandas as pd
import os

def load_data():
    if os.path.exists('salones.csv'):
        return pd.read_csv('salones.csv')
    else:
        salones_data = {
            'Salón': ['A101', 'B202', 'C303', 'D404'],
            'Capacidad': [30, 40, 50, 35],
            'Ubicación': ['Edificio A', 'Edificio B', 'Edificio C', 'Edificio D']
        }
        return pd.DataFrame(salones_data)

def save_data(salones):
    salones.to_csv('salones.csv', index=False)

def app():
    st.title("Modelar Salones - UPCH")

    # Cargar datos de salones
    salones = load_data()

    # Centrar el título de la sección
    st.markdown("<h2 style='text-align: center;'>Salones Disponibles</h2>", unsafe_allow_html=True)
    st.write(salones)
    
    # Permitir agregar nuevos salones
    with st.form(key='add_salon'):
        st.markdown("<h3 style='text-align: center;'>Añadir Nuevo Salón</h3>", unsafe_allow_html=True)
        salon = st.text_input("Salón")
        capacidad = st.number_input("Capacidad", min_value=1)
        ubicacion = st.text_input("Ubicación")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_salon = pd.DataFrame({'Salón': [salon], 'Capacidad': [capacidad], 'Ubicación': [ubicacion]})
            salones = pd.concat([salones, new_salon], ignore_index=True)
            save_data(salones)
            st.success(f"Salón {salon} añadido exitosamente")
            st.experimental_rerun()

    # Mostrar salones actualizados centrados
    st.markdown("<h2 style='text-align: center;'>Salones Actualizados</h2>", unsafe_allow_html=True)
    st.write(salones)

    # Permitir eliminar salones
    with st.form(key='delete_salon'):
        st.markdown("<h3 style='text-align: center;'>Eliminar Salón</h3>", unsafe_allow_html=True)
        salon_to_delete = st.selectbox("Selecciona un salón para eliminar", salones['Salón'])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            salones = salones[salones['Salón'] != salon_to_delete]
            save_data(salones)
            st.success(f"Salón {salon_to_delete} eliminado exitosamente")
            st.experimental_rerun()

if __name__ == '__main__':
    app()
