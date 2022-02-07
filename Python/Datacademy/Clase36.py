
datos_usuarios=[0]

datos_usuarios.append(str(input('Escribe tu primer nombre: ')))
datos_usuarios.append(str(input('Escribe tu primer apellido: ')))
datos_usuarios.append(int(input('Ingresa tu edad: ')))
datos_usuarios.append(float(input('¿Cual fue tu promedio de grado?: ')))

for objetos in datos_usuarios:
    print(objetos)
    
    
print(datos_usuarios) 

#Las listas tienen las mismas propiedades de los strings por lo que usando el -1 se puede reversar el orden de los contenidos
datos_usuarios[::-1]

