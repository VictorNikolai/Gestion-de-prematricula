import streamlit as st
import pandas as pd

def app():
    st.title("Modelar Cursos - UPCH")

    # Cargar datos desde el archivo CSV
    data = pd.read_csv("database.csv")

    st.subheader("Cursos por Ciclo")
    for ciclo in data["CICLO"].unique():
        cursos = data[data["CICLO"] == ciclo]
        st.write(f"### {ciclo}")
        st.write(cursos)
    
    # Permitir agregar nuevos cursos
    with st.form(key='add_curso'):
        st.write("### Añadir Nuevo Curso")
        curso = st.text_input("Curso")
        ciclo = st.text_input("Ciclo")
        prerrequisito = st.text_input("Prerrequisito")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_curso = {'Curso': curso, 'Ciclo': ciclo, 'Prerrequisito': prerrequisito}
            data = data.append(new_curso, ignore_index=True)
            st.success(f"Curso {curso} añadido exitosamente")

    st.write("## Cursos Actualizados")
    st.write(data)
