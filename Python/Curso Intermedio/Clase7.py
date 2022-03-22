#Listas y diccionarios
def run():
    my_list = [433, "Buenos Dias", False, 7.78]
    my_dict = {"firstname": "Juan Manuel", "lastname": "Marín"}
    
    #Una superlistas es una lista que tiene diccionarios dentro
    super_list = [
        {"firstname": "Juan Manuel", "lastname": "Marín"},
        {"firstname": "Juliana", "lastname": "Suarez"},
        {"firstname": "Maria Jose", "lastname": "Marín"},
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Dua", "lastname": "Lipa"},
    ]
    
    
    #Un superdiccionario incluye multiple listas
    super_dict = {
        "numeros_positivos": [1, 2, 3, 4, 5],
        "numeros_negativos": [-5, -4, -3, -2, -1],
        "numeros_flotantes": [0.7, 7.9, 11.5, 0.22],
    } 
    
    
    #Ahora para imprimir los valores dentro de la superlista se usa un for con la terminación .items
    for list_value in super_list:
        print(list_value["firstname"], "-", list_value["lastname"])
    
    #Ahora para imprimir los valores dentro del superdiccionario se usa un for con la terminación .items
    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()