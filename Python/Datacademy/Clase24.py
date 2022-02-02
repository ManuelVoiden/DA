def conversacion(mensaje):
    print("Hola!, muy buenos dias")
    print(f'Elegiste la opción numero {mensaje}')
    print("Adios.")
    
opcion = int(input('Elige una opción -> 1, 2, 3: '))
if opcion == 1 or opcion==2 or opcion==3:
    conversacion(opcion)
else:
    print("ERROR: No elegiste una de las opciones disponibles, intentalo de nuevo")
    
    
    