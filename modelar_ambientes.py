import streamlit as st
import pandas as pd
import os

def load_data():
    if os.path.exists('ambientes.csv'):
        return pd.read_csv('ambientes.csv')
    else:
        ambientes_data = {
            'Tipo de Ambiente': ['Laboratorio', 'Aula', 'Auditorio'],
            'Descripción': ['Equipado con computadoras', 'Salón de clases estándar', 'Espacio para eventos grandes']
        }
        return pd.DataFrame(ambientes_data)

def save_data(ambientes):
    ambientes.to_csv('ambientes.csv', index=False)

def app():
    st.title("Modelar Tipos de Ambientes - UPCH")

    ambientes = load_data()

    st.write("## Tipos de Ambientes Disponibles")
    st.write(ambientes)
    
    with st.form(key='add_ambiente'):
        st.write("### Añadir Nuevo Tipo de Ambiente")
        tipo = st.text_input("Tipo de Ambiente")
        descripcion = st.text_input("Descripción")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_ambiente = pd.DataFrame({'Tipo de Ambiente': [tipo], 'Descripción': [descripcion]})
            ambientes = pd.concat([ambientes, new_ambiente], ignore_index=True)
            save_data(ambientes)
            st.success(f"Tipo de Ambiente {tipo} añadido exitosamente")
            st.experimental_rerun()
#deleteooo xd 
    with st.form(key='delete_ambiente'):
        st.write("### Eliminar Tipo de Ambiente")
        ambiente_a_eliminar = st.selectbox("Selecciona el Tipo de Ambiente a eliminar", ambientes['Tipo de Ambiente'])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            ambientes = ambientes[ambientes['Tipo de Ambiente'] != ambiente_a_eliminar]
            save_data(ambientes)
            st.success(f"Tipo de Ambiente {ambiente_a_eliminar} eliminado exitosamente")
            st.experimental_rerun()

    st.write("## Tipos de Ambientes Actualizados")
    st.write(ambientes)

if __name__ == '__main__':
    app()
