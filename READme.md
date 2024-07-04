<h1 align="center" id="title">Proyecto de Análisis y Diseño de Algoritmos
<h1 align="center" id="title">Gestión de PreMatricula</h1>

<div align="center">
  <img src="https://cdn.www.gob.pe/uploads/document/file/5540193/880238-logo-sme.png" alt="Descripción de la imagen">
</div>


## Tabla de contenidos:
---
- [Descripción](#Descripción)
- [Integrantes:](#Figma)

## Descripción:

El presente proyecto de sistema tiene como objetivo desarrollar una herramienta informática que apoye a los coordinadores de carrera de la Universidad Peruana Cayetano Heredia (UPCH) en la planificación y gestión de los cursos que se habilitarán para cada ciclo académico.

Como usuarios principales del sistema, los coordinadores de carrera enfrentan diversos desafíos en la organización de la oferta académica, desde la selección de los cursos a aperturar hasta la notificación a los docentes sobre sus horarios. Este proyecto busca brindar una solución tecnológica integral que simplifique y optimice estos procesos clave.


## Integrantes:
- [Saldaña Rodríguez, Sebastián Antonio](sebastian.saldana@upch.pe)
- [More Ayay, Dahayra Xiomara](dahayra.more@upch.pe)
- [Huarcaya Pumacayo, Victor Nikolai](victor.huarcaya@upch.pe)
- [Castro Pichihua, Victoria Beatriz](victoria.castro@upch.pe)
- [Peñaloza Huaman, Bryan Alexander](bryan.penaloza@upch.pe)
- [Mendez Cruz, Ciara Solange](ciara.mendez@upch.pe)
- [Siccha Huayanay, Valery Krystal](valery.siccha@upch.pe)
- [Rodriguez Reategui, Rodrigo](rodrigo.rodriguez.r@upch.pe)
- [Mejia Lopez, Leonardo Camilo](leonardo.mejia.l@upch.pe)





## Código de Diagrama de Clase
<details><summary> <b>Expand</b> </summary>

``` shell
@startuml

class Curso {
    - nombre: String
    - ciclo: String
    - prerrequisito: String
}

class Salon {
    - nombre: String
    - capacidad: int
    - ubicacion: String
}

class Ambiente {
    - tipo: String
    - descripcion: String
}

class Alumno {
    - nombre: String
}

class Asignacion {
    - alumno: Alumno
    - curso: Curso
}

class Horario {
    - cursos: List<Curso>
    - num_horas: int
    - num_salones: int
    - requisitos: List<Requerimiento>
    + cromosoma_aleatorio(): int[]
    + fitness(): int
    + crossover(): (int[], int[])
    + mutacion(): int[]
    + poblacion_aleatoria(): int[]
    + fitness_poblacion(): int[]
    + optimizar_horarios(): (int[], int)
}

class Requerimiento {
    - curso: Curso
    - tipo_ambiente: String
}

class Login {
    - usuario: String
    - contraseña: String
    + autenticar(usuario: String, contraseña: String): boolean
}

class MultiApp {
    + apps: List<Application>
    + add_app(titulo: String, funcion: Function)
    + run()
}

interface Application {
    run()
}

Curso "1" -down-> "1..*" Alumno: asignado a
Asignacion "1" -- "1" Alumno: tiene
Asignacion "1" -- "1" Curso: tiene
Curso "1..*" -up-> "1" Salon: se realiza en
Curso "1" -right-> "1" Ambiente: requiere
Horario "1" -- "1..*" Curso: contiene
Horario "1" -- "1..*" Requerimiento: contiene
Requerimiento "1" -- "1" Curso: tiene
Requerimiento "1" -- "1" Ambiente: tiene
Login "1" -down-> "1" MultiApp: permite acceso

@enduml

```
<p align="center">
  <img src="https://github.com/Victor-Nikolai/Recursos/blob/main/Diagrama%20de%20Clase%20.png" alt="image">
</p>
