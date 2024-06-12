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
            new_salon = pd.DataFrame({'Salón': [salon], 'Capacidad': [capacidad], 'Ubicación': [ubicacion]})
            salones = pd.concat([salones, new_salon], ignore_index=True)
            save_data(salones)
            st.success(f"Salón {salon} añadido exitosamente")
            st.experimental_rerun()

    st.write("## Salones Actualizados")
    st.write(salones)

if __name__ == '__main__':
    app()
