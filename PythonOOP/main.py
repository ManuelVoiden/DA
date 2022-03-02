from car import Car  #Se debe importar los archivos de los que vamos a sacar datos
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    #car = Car()
    #car.license = "PQR325"
    #car.driver = "Juan Manuel Marín Bedoya"
    #print(vars(car))
    
    #car2 = Car()
    #car2.license = "PAR377"
    #car2.driver = "Luis Mario Marín Bedoya"
    #print(vars(car2))
        
    car3 = Car("BTU908", Account(1, "Juliana Suarez Avila", 1005413227, "juliuwu@gmail.com", "ajiacoajiaco")) #Aqui se puede ver otra forma de introducir datos al objeto car
    print(vars(car3))
    print(vars(car3.driver))
    