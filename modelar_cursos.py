import streamlit as st
import pandas as pd

def save_data(data, file_path):
    data.to_csv(file_path, index=False)

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

    with st.form(key='delete_curso'):
        st.write("### Eliminar curso actualizado")
        curso_a_eliminar = st.selectbox("Selecciona el curso a eliminar",data['NOMBRE DE LA ASIGNATURA'] if 'NOMBRE DE LA ASIGNATURA' in data else [])
        submit_delete = st.form_submit_button("Eliminar")

        if submit_delete:
            data = data[data['NOMBRE DE LA ASIGNATURA'] != curso_a_eliminar]
            save_data(data, 'database.csv')
            st.success(f"NOMBRE DE LA ASIGNATURA '{curso_a_eliminar}' eliminado exitosamente")
    

if __name__ == "__main__":
    app()
