#Uso de diccionarios en Python

def run():
    
    mi_diccionario = {
        'llave_uno': 1,
        'llave_dos': 2,
        'llave_tres': 3,
    }

    print(mi_diccionario['llave_dos'])
          

    poblacion_paises = {
        'Argentina': 45550000,
        'Brasil': 215000000,
        'Colombia': 48650000,
        'Chile': 38535000,
    }
    
    #Para imprimir uno de las poblaciones hago lo siguiente
    print(poblacion_paises['Colombia'])
    
    #Usando un for para imprimir todos los nombres de paises
    for pais in poblacion_paises.keys():
        print(pais)
        
    
    #Usando un for para imprimir todos los valores poblacionales
    for poblacion in poblacion_paises.values():
        print(poblacion)
        
        
    
    #Usando un for para imprimir tanto los nombres de paises como la población
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes.')
    


if __name__ == '__main__':
    run()