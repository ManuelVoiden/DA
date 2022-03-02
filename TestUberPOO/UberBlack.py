from car import Car

class UberBlack(Car):  #Se aplica Herencia en estos archivos
    brand = str
    model = str
    
    def __init__(self, license, driver, brand, model):
        super.__init(license, driver) #Aqui se esta haciendo un __init__ anidado, se llaman los datos de license y driver desde Car, los otros dos datos son propios de el tipo de Uber
        self.brand = brand
        self.model = model