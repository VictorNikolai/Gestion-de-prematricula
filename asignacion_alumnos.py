import streamlit as st
import pandas as pd

def app():
    st.title("Asignación de Alumnos a Cursos - UPCH")

    # Datos de ejemplo para asignación de alumnos
    asignacion_data = {
        'Alumno': ['Juan Pérez', 'Ana García', 'Luis Fernández'],
        'Curso Asignado': ['Matemáticas', 'Física', 'Química']
    }

    asignacion = pd.DataFrame(asignacion_data)

    st.write("## Asignación de Alumnos a Cursos")
    st.write(asignacion)
    
    # Permitir agregar nuevas asignaciones
    with st.form(key='add_asignacion'):
        st.write("### Añadir Nueva Asignación")
        alumno = st.text_input("Alumno")
        curso = st.text_input("Curso Asignado")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_asignacion = {'Alumno': alumno, 'Curso Asignado': curso}
            asignacion = asignacion.append(new_asignacion, ignore_index=True)
            st.success(f"Asignación para {alumno} añadido exitosamente")

    st.write("## Asignaciones Actualizadas")
    st.write(asignacion)
