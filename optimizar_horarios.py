import streamlit as st
import pandas as pd
import numpy as np
import random
import os

def app():
    st.title("Optimización de Horarios")

    malla_curricular_path = 'datainginfo.csv'
    historial_academico_path = 'ALUMNO1.csv'

    malla_curricular = pd.read_csv(malla_curricular_path)
    historial_academico = pd.read_csv(historial_academico_path)

    np.random.seed(0)

    # Función para generar horarios
    def generar_horario():
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        inicio = np.random.choice(range(7, 21))  # Hora de inicio entre 7am y 9pm (21h)
        duracion = np.random.choice([2, 3])  # Duración de la clase de 2 o 3 horas
        fin = inicio + duracion
        dia = np.random.choice(dias)
        return f"{dia} {inicio}-{fin}h"

    # Generar nombres de docentes y aulas de forma aleatoria
    docentes = [f"Docente_{i}" for i in range(1, 101)]
    aulas = [f"Aula_{i}" for i in range(1, 101)]

    # Aplicar la generación de horarios a la malla curricular
    malla_curricular['HORARIO'] = [generar_horario() for _ in range(malla_curricular.shape[0])]
    malla_curricular['DOCENTE'] = np.random.choice(docentes, size=malla_curricular.shape[0])
    malla_curricular['AULA'] = np.random.choice(aulas, size=malla_curricular.shape[0])

    # Definir la ruta del archivo
    horarios_dir = '/content'
    horarios_path = os.path.join(horarios_dir, 'HorariosCursos.csv')

    # Crear el directorio si no existe
    if not os.path.exists(horarios_dir):
        os.makedirs(horarios_dir)

    # Guardar el nuevo archivo con horarios
    malla_curricular.to_csv(horarios_path, index=False)

    # malla_curricular.head()
    malla_curricular  # malla curricular completa

    # Identificar los cursos que el estudiante ya ha aprobado
    cursos_aprobados = set(historial_academico['CODIGO'])

    # Filtrar la malla curricular para encontrar los cursos que el estudiante aún no ha tomado
    cursos_disponibles = malla_curricular[~malla_curricular['CODIGO'].isin(cursos_aprobados)]

    # Verificar prerrequisitos
    def prerrequisitos_cumplidos(row, cursos_aprobados):
        prerrequisitos = row['PRE REQUISITO'].split(',')
        if 'NINGUNO' in prerrequisitos:
            return True
        return all(prerrequisito in cursos_aprobados for prerrequisito in prerrequisitos)

    # Filtrar cursos para los que el estudiante cumple con los prerrequisitos
    cursos_posibles = cursos_disponibles[cursos_disponibles.apply(lambda row: prerrequisitos_cumplidos(row, cursos_aprobados), axis=1)]

    # Mostrar cursos posibles que el estudiante puede tomar
    cursos_posibles[['CODIGO', 'NOMBRE DE LA ASIGNATURA', 'CREDITOS', 'PRE REQUISITO', 'HORARIO']]

    # Función para convertir horarios en un formato manejable
    def parse_horario(horario):
        dia, horas = horario.split()
        inicio, fin = map(int, horas[:-1].split('-'))
        return dia, inicio, fin

    # Parámetros del algoritmo genético
    num_generaciones = 50
    tamano_poblacion = 100
    tasa_cruzamiento = 0.8
    tasa_mutacion = 0.1
    max_creditos = 22

    # Cargar el DataFrame 'cursos_posibles'
    # Asegúrate de cargar tu DataFrame aquí, por ejemplo:
    # cursos_posibles = pd.read_csv('ruta_a_tu_archivo.csv')

    # Aplicar la función parse_horario de manera segura
    cursos_posibles.loc[:, 'HORARIO PARSED'] = cursos_posibles['HORARIO'].apply(parse_horario)

    # Función para generar un individuo (horario)
    def generar_individuo():
        cursos_elegidos = []
        for _, curso in cursos_posibles.iterrows():
            if random.random() < 0.5:  # 50% de probabilidad de incluir cada curso
                cursos_elegidos.append(curso)
        return cursos_elegidos

    # Función de fitness
    def evaluar_fitness(individuo):
        total_creditos = sum(curso['CREDITOS'] for curso in individuo)
        if total_creditos > max_creditos:
            return -1  # Penalización por exceder el máximo de créditos

        # Verificar superposiciones de horario
        horarios = [(curso['HORARIO PARSED'], curso['CREDITOS']) for curso in individuo]
        penalizacion = 0
        premiacion = 0

        for i in range(len(horarios)):
            for j in range(i + 1, len(horarios)):
                if horarios[i][0][0] == horarios[j][0][0]:  # Mismo día
                    if not (horarios[i][0][2] <= horarios[j][0][1] or horarios[i][0][1] >= horarios[j][0][2]):
                        penalizacion += 10  # Penalización por superposición de horarios

        # Penalizaciones por horarios no deseados
        for horario, creditos in horarios:
            dia, inicio, fin = horario
            if fin > 20:  # Curso termina después de las 8pm
                penalizacion += 5
            if inicio < 8 or fin > 20:  # Penalización por terminar después de la hora límite
                penalizacion += 3
            if 12 <= inicio <= 14:  # Curso durante el almuerzo
                penalizacion += 2

        # Penalización por huecos entre clases
        dias = set(horario[0] for horario in horarios)
        for dia in dias:
            clases_dia = sorted((h for h in horarios if h[0][0] == dia), key=lambda x: x[0][1])
            for i in range(len(clases_dia) - 1):
                if clases_dia[i][0][2] < clases_dia[i + 1][0][1]:  # Hueco entre clases
                    penalizacion += (clases_dia[i + 1][0][1] - clases_dia[i][0][2]) * 0.5

        # Premiaciones por horarios deseados
        for horario, creditos in horarios:
            dia, inicio, fin = horario
            if 8 <= inicio <= 11:  # Clases en la mañana
                premiacion += 2
            if 14 <= inicio <= 18:  # Clases en la tarde temprano
                premiacion += 1

        return total_creditos - penalizacion + premiacion  # Maximizar créditos minimizando penalizaciones

    # Generar población inicial y evaluar
    poblacion = [generar_individuo() for _ in range(tamano_poblacion)]
    fitness_scores = [evaluar_fitness(individuo) for individuo in poblacion]

    # Identificar y mostrar la mejor solución inicial
    mejor_individuo = poblacion[fitness_scores.index(max(fitness_scores))]
    mejor_fitness = max(fitness_scores)

    # Convertir el mejor individuo a un DataFrame para visualización
    mejor_horario_df = pd.DataFrame(mejor_individuo)
    mejor_horario_df = mejor_horario_df[['CICLO', 'CODIGO', 'NOMBRE DE LA ASIGNATURA', 'CREDITOS', 'HORARIO', 'DOCENTE', 'AULA']]

    mejor_horario_df

    st.write(f"Mejor Solución (Fitness: {mejor_fitness}):")
    st.write(mejor_horario_df)

    st.write("### Visualización de Horario")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]:
        st.write(f"#### {dia}")
        cursos_en_dia = mejor_horario_df[mejor_horario_df['HORARIO'].str.startswith(dia)]
        if not cursos_en_dia.empty:
            st.write(cursos_en_dia[['CODIGO', 'NOMBRE DE LA ASIGNATURA', 'HORARIO', 'DOCENTE', 'AULA']])
        else:
            st.write("No hay cursos en este día.")

if __name__ == "__main__":
    app()
