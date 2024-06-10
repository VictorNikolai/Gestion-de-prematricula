import streamlit as st
import pandas as pd

def app():
    st.title("Modelar Salones - UPCH")

    # Datos de ejemplo para salones
    salones_data = {
        'Salón': ['A101', 'B202', 'C303', 'D404'],
        'Capacidad': [30, 40, 50, 35],
        'Ubicación': ['Edificio A', 'Edificio B', 'Edificio C', 'Edificio D']
    }

    salones = pd.DataFrame(salones_data)

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
            new_salon = {'Salón': salon, 'Capacidad': capacidad, 'Ubicación': ubicacion}
            salones = salones.append(new_salon, ignore_index=True)
            st.success(f"Salón {salon} añadido exitosamente")

    st.write("## Salones Actualizados")
    st.write(salones)
