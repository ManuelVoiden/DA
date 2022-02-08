import numpy as np

vector= np.array([3, 7, 8, 14, 256])
print(vector)

vector_str = np.array(["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre"])
print(vector_str)

matriz = np.array([[25, 50],[16, 32]])
print(matriz)

type(vector)
type(matriz)

print(vector.shape)
print(matriz.shape)
print(vector_str.shape)

vector_str.dtype
