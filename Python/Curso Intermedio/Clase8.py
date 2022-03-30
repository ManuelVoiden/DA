maximo = 0
maximo = int(input("Hola!, Ingrese el numero maximo al cual desea sacarle el cuadrado: "))


def cuadrados():
    numeros_cuadrados = []
    for i in range(1, maximo):
        numeros_cuadrados.append(i**2)
        
    print(numeros_cuadrados)
    
    
    
def cuadrados_divisibles():
    numeros_cuadrados_divisibles = []
    for i in range(1, maximo):
        if i%3 != 0:
            numeros_cuadrados_divisibles.append(i**2)
    
    print(numeros_cuadrados_divisibles)
    
    
    
    
    
if __name__ == '__main__':
    cuadrados()
    cuadrados_divisibles()
    