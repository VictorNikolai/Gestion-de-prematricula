import streamlit as st
import pandas as pd

def app():
    st.title("Modelar Requerimientos de Ambientes - UPCH")

    # Inicializar requerimientos en session_state si no existe
    if 'requerimientos' not in st.session_state:
        requerimientos_data = {
            'Curso': ['Matemáticas', 'Física', 'Química'],
            'Tipo de Ambiente Requerido': ['Aula', 'Laboratorio', 'Laboratorio']
        }
        st.session_state.requerimientos = pd.DataFrame(requerimientos_data)

    st.write("## Requerimientos de Ambientes por Curso")
    st.write(st.session_state.requerimientos)
    
    # Permitir agregar nuevos requerimientos de ambientes
    with st.form(key='add_requerimiento'):
        st.write("### Añadir Nuevo Requerimiento")
        curso = st.text_input("Curso")
        tipo_ambiente = st.text_input("Tipo de Ambiente Requerido")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_requerimiento = pd.DataFrame({'Curso': [curso], 'Tipo de Ambiente Requerido': [tipo_ambiente]})
            st.session_state.requerimientos = pd.concat([st.session_state.requerimientos, new_requerimiento], ignore_index=True)
            st.success(f"Requerimiento para {curso} añadido exitosamente")

    st.write("## Requerimientos de Ambientes Actualizados")
    st.write(st.session_state.requerimientos)

if __name__ == "__main__":
    app()


