import pandas as pd

df_estudiantes = pd.read_csv('studentsperformance_f29e92e5-811f-4cf9-9504-91644b0ecc35.csv')
print(df_estudiantes)

df_estudiantes.head()
df_estudiantes.tail()
df_estudiantes.sample(7)
print(df_estudiantes.shape)
df_estudiantes.describe()