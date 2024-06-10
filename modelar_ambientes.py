import streamlit as st
import pandas as pd

def app():
    st.title("Modelar Tipos de Ambientes - UPCH")

    # Datos de ejemplo para tipos de ambientes
    ambientes_data = {
        'Tipo de Ambiente': ['Laboratorio', 'Aula', 'Auditorio'],
        'Descripción': ['Equipado con computadoras', 'Salón de clases estándar', 'Espacio para eventos grandes']
    }

    ambientes = pd.DataFrame(ambientes_data)

    st.write("## Tipos de Ambientes Disponibles")
    st.write(ambientes)
    
    # Permitir agregar nuevos tipos de ambientes
    with st.form(key='add_ambiente'):
        st.write("### Añadir Nuevo Tipo de Ambiente")
        tipo = st.text_input("Tipo de Ambiente")
        descripcion = st.text_input("Descripción")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_ambiente = {'Tipo de Ambiente': tipo, 'Descripción': descripcion}
            ambientes = ambientes.append(new_ambiente, ignore_index=True)
            st.success(f"Tipo de Ambiente {tipo} añadido exitosamente")

    st.write("## Tipos de Ambientes Actualizados")
    st.write(ambientes)
