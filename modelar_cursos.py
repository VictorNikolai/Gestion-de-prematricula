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
        NOMBRE_DE_LA_ASIGNATURA = st.text_input("NOMBRE DE LA ASIGNATURA")
        CICLO = st.text_input("CICLO")
        CÓDIGO = st.text_input("CÓDIGO")
        PRE_REQUISITO = st.text_input("PRE REQUISITO")
        CRÉDITOS = st.text_input("CRÉDITOS")
        MODALIDAD = st.text_input("MODALIDAD")
        submit = st.form_submit_button("Añadir")

        if submit:
            new_curso = pd.DataFrame({'NOMBRE DE LA ASIGNATURA': [NOMBRE_DE_LA_ASIGNATURA], 'CICLO': [CICLO], 'PRE REQUISITO': [PRE_REQUISITO], 'CRÉDITOS': [CRÉDITOS], 'MODALIDAD': [MODALIDAD], 'CÓDIGO': [CÓDIGO]})
            data = pd.concat([data, new_curso], ignore_index=True)
            data.to_csv("database.csv", index=False)  # Guardar los cambios
            st.success(f"Curso {NOMBRE_DE_LA_ASIGNATURA} añadido exitosamente")

    st.write("## Cursos Actualizados")
    st.write(data)

if __name__ == "__main__":
    app()
