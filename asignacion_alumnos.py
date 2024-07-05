import streamlit as st
import pandas as pd

def app():
    st.title("Asignación de Alumnos a Cursos - UPCH")

    # Inicializar asignaciones en session_state si no existe
    if 'asignacion' not in st.session_state:
        asignacion_data = {
            'Alumno': ['Juan Pérez', 'Ana García', 'Luis Fernández'],
            'Curso Asignado': ['Matemáticas', 'Física', 'Química']
        }
        st.session_state.asignacion = pd.DataFrame(asignacion_data)

    st.write("## Asignación de Alumnos a Cursos")
    st.write(st.session_state.asignacion)
    
    # Permitir agregar nuevas asignaciones
    with st.form(key='add_asignacion'):
        st.write("### Añadir Nueva Asignación")
        alumno = st.text_input("Alumno")
        curso = st.text_input("Curso Asignado")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_asignacion = pd.DataFrame({'Alumno': [alumno], 'Curso Asignado': [curso]})
            st.session_state.asignacion = pd.concat([st.session_state.asignacion, new_asignacion], ignore_index=True)
            st.success(f"Asignación para {alumno} añadida exitosamente")

    st.write("## Asignaciones Actualizadas")
    st.write(st.session_state.asignacion)

if __name__ == "__main__":
    app()

