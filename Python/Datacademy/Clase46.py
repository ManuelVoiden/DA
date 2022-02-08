import pandas as pd

dic_estudiantes = {
    'nombre': ["Camilo", "Maria", "Juan", "Ana", "Andres", "Juliana", "Esteban", "Alejandro"],
    'Edad': [24, 27, 21, 24, 24, 23, 28, 22],
    'Puesto': ["Data Analyst", "Data Engineer", "ML Engineer", "DevOps", "Data Analyst", "Data Scientist", "Data Engineer", "Data Analyst"],
}

bd_estudiantes = pd.DataFrame(dic_estudiantes)
print(bd_estudiantes)
print(bd_estudiantes.dtypes)




























