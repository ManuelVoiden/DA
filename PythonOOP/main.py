from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    
    car = Car()
    car.license = "PQR325"
    car.driver = "Juan Manuel Marín Bedoya"
    print(vars(car))
    
    car2 = Car()
    car2.license = "PAR377"
    car2.driver = "Luis Mario Marín Bedoya"
    print(vars(car2))