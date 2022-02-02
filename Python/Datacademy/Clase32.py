from sqlalchemy import false


def run():
    x=0
    aux=0
    
    print('Bienvenido a la calculadora de pontencias! 👨‍🔬👩‍🔬')  
    limite = int(input('Ingresa el valor limite al que puede llegar la potencia: '))
    
    while aux < 1: 
        x=x+1
        contador=2**x
        
        if 2**(x+1)>limite:
            potencia=x
            aux=1
        else:
            aux=0
            
    print(f'Se ha alcanzado el limite y el resultado es {contador}, la potencia mas alta de 2 antes de llegar a {limite} fue de {potencia}')
            


if __name__ == '__main__':
    run()