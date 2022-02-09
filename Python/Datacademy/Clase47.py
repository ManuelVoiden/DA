import pandas as pd

df_estudiantes = pd.read_csv('studentsperformance_f29e92e5-811f-4cf9-9504-91644b0ecc35.csv')
print(df_estudiantes)

df_estudiantes.head()
df_estudiantes.tail()
df_estudiantes.sample(7) #Aqui se puede sacar una muestra random de la bd
print(df_estudiantes.shape)
df_estudiantes.describe() #Aqui se puede sacar un rapido analisis de las columnas con numeros en la bd