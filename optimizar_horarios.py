import streamlit as st
import pandas as pd
import numpy as np
import random

def app():
    st.title("Optimización de Horarios")

    malla_curricular_path = 'datainginfo.csv'
    historial_academico_path = 'ALUMNO1.csv'

    malla_curricular = pd.read_csv(malla_curricular_path)
    historial_academico = pd.read_csv(historial_academico_path)

    np.random.seed(0)

    def generar_horario():
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        inicio = np.random.choice(range(7, 21))
        duracion = np.random.choice([2, 3])
        fin = inicio + duracion
        dia = np.random.choice(dias)
        return f"{dia} {inicio}-{fin}h"

    docentes = [f"Docente_{i}" for i in range(1, 101)]
    aulas = [f"Aula_{i}" for i in range(1, 101)]

    malla_curricular['HORARIO'] = [generar_horario() for _ in range(malla_curricular.shape[0])]
    malla_curricular['DOCENTE'] = np.random.choice(docentes, size=malla_curricular.shape[0])
    malla_curricular['AULA'] = np.random.choice(aulas, size=malla_curricular.shape[0])

    cursos_aprobados = set(historial_academico['CODIGO'])

    def prerrequisitos_cumplidos(row, cursos_aprobados):
        prerrequisitos = row['PRE REQUISITO'].split(',')
        if 'NINGUNO' in prerrequisitos:
            return True
        return all(prerrequisito in cursos_aprobados for prerrequisito in prerrequisitos)

    cursos_disponibles = malla_curricular[~malla_curricular['CODIGO'].isin(cursos_aprobados)]
    cursos_posibles = cursos_disponibles[cursos_disponibles.apply(lambda row: prerrequisitos_cumplidos(row, cursos_aprobados), axis=1)]

    num_generaciones = 50
    tamano_poblacion = 100
    tasa_cruzamiento = 0.8
    tasa_mutacion = 0.1
    max_creditos = 22

    def parse_horario(horario):
        dia, horas = horario.split()
        inicio, fin = map(int, horas[:-1].split('-'))
        return dia, inicio, fin

    cursos_posibles['HORARIO PARSED'] = cursos_posibles['HORARIO'].apply(parse_horario)

    def generar_individuo():
        cursos_elegidos = []
        for _, curso in cursos_posibles.iterrows():
            if random.random() < 0.5:
                cursos_elegidos.append(curso)
        return cursos_elegidos

    def evaluar_fitness(individuo):
        total_creditos = sum(curso['CREDITOS'] for curso in individuo)
        if total_creditos > max_creditos:
            return -1

        horarios = [(curso['HORARIO PARSED'], curso['CREDITOS']) for curso in individuo]
        for i in range(len(horarios)):
            for j in range(i + 1, len(horarios)):
                if horarios[i][0][0] == horarios[j][0][0]:
                    if not (horarios[i][0][2] <= horarios[j][0][1] or horarios[i][0][1] >= horarios[j][0][2]):
                        return -1

        penalizacion = 0
        for horario, creditos in horarios:
            dia, inicio, fin = horario
            if fin > 19:
                penalizacion += 5
            if 12 <= inicio <= 14:
                penalizacion += 2

        dias = set(horario[0] for horario in horarios)
        for dia in dias:
            clases_dia = sorted((h for h in horarios if h[0][0] == dia), key=lambda x: x[0][1])
            for i in range(len(clases_dia) - 1):
                if clases_dia[i][0][2] < clases_dia[i + 1][0][1]:
                    penalizacion += (clases_dia[i + 1][0][1] - clases_dia[i][0][2]) * 0.5

        premiacion = 0
        for horario, creditos in horarios:
            dia, inicio, fin = horario
            if 8 <= inicio <= 11:
                premiacion += 2
            if 14 <= inicio <= 18:
                premiacion += 1

        return total_creditos - penalizacion + premiacion

    poblacion = [generar_individuo() for _ in range(tamano_poblacion)]
    fitness_scores = [evaluar_fitness(individuo) for individuo in poblacion]

    mejor_individuo = poblacion[fitness_scores.index(max(fitness_scores))]
    mejor_fitness = max(fitness_scores)

    for generacion in range(num_generaciones):
        nueva_poblacion = []
        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = random.choices(poblacion, k=2)
            if random.random() < tasa_cruzamiento:
                punto_cruce = random.randint(1, len(padre1) - 1)
                hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
                hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
            else:
                hijo1, hijo2 = padre1, padre2

            if random.random() < tasa_mutacion and len(hijo1) > 0:
                idx = random.randint(0, len(hijo1) - 1)
                hijo1[idx] = cursos_posibles.iloc[random.randint(0, len(cursos_posibles) - 1)]
            if random.random() < tasa_mutacion and len(hijo2) > 0:
                idx = random.randint(0, len(hijo2) - 1)
                hijo2[idx] = cursos_posibles.iloc[random.randint(0, len(cursos_posibles) - 1)]

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion
        fitness_scores = [evaluar_fitness(individuo) for individuo in poblacion]

        mejor_individuo_generacion = poblacion[fitness_scores.index(max(fitness_scores))]
        mejor_fitness_generacion = max(fitness_scores)

        if mejor_fitness_generacion > mejor_fitness:
            mejor_individuo = mejor_individuo_generacion
            mejor_fitness = mejor_fitness_generacion

    mejor_horario_df = pd.DataFrame(mejor_individuo)
    mejor_horario_df = mejor_horario_df[['CICLO', 'CODIGO', 'NOMBRE DE LA ASIGNATURA', 'CREDITOS', 'HORARIO', 'DOCENTE', 'AULA']]

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
