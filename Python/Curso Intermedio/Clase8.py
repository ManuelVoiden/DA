maximo = 0
maximo = int(input("Hola!, Ingrese el numero maximo al cual desea sacarle el cuadrado: "))


def cuadrados():
    numeros_cuadrados = []
    for i in range(1, maximo):
        numeros_cuadrados.append(i**2)
        
    print(numeros_cuadrados)
    

##Metodo tradicional sin list comprehensions    
def cuadrados_divisibles():
    numeros_cuadrados_divisibles = []
    for i in range(1, maximo):
        if i%3 != 0:
            numeros_cuadrados_divisibles.append(i**2)
    
    print(numeros_cuadrados_divisibles)
    
    
    
##Nuevo metodo con list comprehensions    
def nuevo_cuadrados_divisibles():
    nuevo_numeros_cuadrados_divisibles = [i**2 for i in range(1, maximo) if i%3 != 0]
    ##Esto sigue la estructura de:
    ##[elemento for elemento in iterable if condicion]
    print(nuevo_numeros_cuadrados_divisibles)
    
    
##Reto de la clase
##Crear una lista de todos los multiplos de 4 que a la vez son multiplos de 6 y de 9, maximo 5 cifras
def tarea():
    lista_tarea = [i for i in range(1, 99999) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(lista_tarea)

    
    
if __name__ == '__main__':
    cuadrados()
    cuadrados_divisibles()
    nuevo_cuadrados_divisibles()
    tarea()
    