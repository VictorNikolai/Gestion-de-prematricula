import streamlit as st
import numpy as np
import pandas as pd  # Asegúrate de importar pandas

def app():
    st.title("Optimización de Horarios")

    # Parámetros del problema
    num_cursos = 10  # Ejemplo de número de cursos
    num_horas = 8
    num_salones = 5
    requisitos = [{'horario': i % num_horas, 'salon': i % num_salones} for i in range(num_cursos)]
    
    # Nombres de los cursos para ejemplo
    nombres_cursos = [f"Curso {i+1}" for i in range(num_cursos)]
    
    def cromosoma_aleatorio(num_cursos, num_horas, num_salones):
        return np.random.randint(0, num_horas * num_salones, num_cursos)

    def fitness(cromosoma, num_cursos, num_horas, num_salones, requisitos):
        puntuacion = 0
        for i in range(num_cursos):
            horario = cromosoma[i] // num_salones
            salon = cromosoma[i] % num_salones
            if requisitos[i]['horario'] == horario and requisitos[i]['salon'] == salon:
                puntuacion += 1
        return puntuacion

    def crossover(p1, p2, num_cursos):
        corte = np.random.randint(1, num_cursos)
        h1 = np.concatenate([p1[:corte], p2[corte:]])
        h2 = np.concatenate([p2[:corte], p1[corte:]])
        return h1, h2

    def mutacion(cromosoma, num_cursos):
        alelo = np.random.randint(0, num_cursos)
        cromosoma[alelo] = np.random.randint(0, num_horas * num_salones)
        return cromosoma

    def poblacion_aleatoria(P, num_cursos, num_horas, num_salones):
        return np.array([cromosoma_aleatorio(num_cursos, num_horas, num_salones) for _ in range(P)])

    def fitness_poblacion(poblacion, num_cursos, num_horas, num_salones, requisitos):
        return np.array([fitness(individuo, num_cursos, num_horas, num_salones, requisitos) for individuo in poblacion])

    def optimizar_horarios(num_cursos, num_horas, num_salones, requisitos):
        P = 1000
        PORCENTAJE_SELECCION = 0.5
        SELECCION = int(P * PORCENTAJE_SELECCION)
        PROB_MUTACION = 0.01

        poblacion = poblacion_aleatoria(P, num_cursos, num_horas, num_salones)
        valores_fitness = fitness_poblacion(poblacion, num_cursos, num_horas, num_salones, requisitos)
        mejor_fitness = 0
        mejor_solucion = None

        for generacion in range(100):  # Número de generaciones
            poblacion_seleccionada = poblacion[valores_fitness.argsort()[::-1][:SELECCION]]
            descendencia = []
            for i in range(SELECCION // 2):
                idx1, idx2 = np.random.randint(0, SELECCION, 2)
                p1, p2 = poblacion_seleccionada[idx1], poblacion_seleccionada[idx2]
                h1, h2 = crossover(p1, p2, num_cursos)
                if np.random.rand() < PROB_MUTACION:
                    h1 = mutacion(h1, num_cursos)
                if np.random.rand() < PROB_MUTACION:
                    h2 = mutacion(h2, num_cursos)
                descendencia.append(h1)
                descendencia.append(h2)
            descendencia = np.array(descendencia)
            poblacion = np.concatenate([poblacion_seleccionada, descendencia], axis=0)
            valores_fitness = fitness_poblacion(poblacion, num_cursos, num_horas, num_salones, requisitos)
            mejor_indice = np.argmax(valores_fitness)
            if valores_fitness[mejor_indice] > mejor_fitness:
                mejor_fitness = valores_fitness[mejor_indice]
                mejor_solucion = poblacion[mejor_indice]

        return mejor_solucion, mejor_fitness

    mejor_solucion, fitness_max = optimizar_horarios(num_cursos, num_horas, num_salones, requisitos)
    
    # Crear el horario basado en la mejor solución
    horario = []
    for i in range(num_cursos):
        horario_curso = {
            "Curso": nombres_cursos[i],
            "Hora": mejor_solucion[i] // num_salones,
            "Salón": mejor_solucion[i] % num_salones
        }
        horario.append(horario_curso)
    
    # Mostrar la mejor solución
    st.write(f"Mejor Solución: {mejor_solucion}")
    st.write(f"Fitness: {fitness_max}")

    # Mostrar el horario
    st.write("## Horario Optimizado")
    horario_df = pd.DataFrame(horario)
    st.write(horario_df)

    st.write("### Visualización de Horario")
    for i in range(num_horas):
        st.write(f"### Hora {i}")
        cursos_en_hora = horario_df[horario_df["Hora"] == i]
        if not cursos_en_hora.empty:
            st.write(cursos_en_hora)
        else:
            st.write("No hay cursos en esta hora.")

