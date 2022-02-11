import pandas as pd

df_estudiantes = pd.read_csv('studentsperformance.csv')
print(df_estudiantes)

df_estudiantes.head()
df_estudiantes.tail()
df_estudiantes.sample(7) #Aqui se puede sacar una muestra random de la bd
print(df_estudiantes.shape)
df_estudiantes.describe() #Aqui se puede sacar un rapido analisis de las columnas con numeros en la bd

df_estudiantes.columns #Así se pueden leer los nombres de las columnas de la bd
df_estudiantes['math score']

#Se puede entonces analizar rapidamente cada columna de la siguiente manera:

df_estudiantes['math score'].mean()
print(df_estudiantes['math score'].mean())

df_estudiantes['math score'].median()
print(df_estudiantes['math score'].median())

df_estudiantes['math score'].std()
print(df_estudiantes['math score'].std())