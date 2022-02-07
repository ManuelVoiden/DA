
datos_usuarios=[0]

datos_usuarios.append(str(input('Escribe tu primer nombre: ')))
datos_usuarios.append(str(input('Escribe tu primer apellido: ')))
datos_usuarios.append(int(input('Ingresa tu edad: ')))
datos_usuarios.append(float(input('¿Cual fue tu promedio de grado?: ')))

for objetos in datos_usuarios:
    print(objetos)
    
    
print(datos_usuarios) 
datos_usuarios[::-1]

