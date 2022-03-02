from account import Account

class Car:
    id = int
    license = str
    driver = Account("", "", "", "", "")   ##Se declara driver = Account ya que importamos el archivo account.py, esto permite vincular directamente ambos archivos
    passenger = int
    
    def __init__(self, license, driver):
        self.license = license
        self.driver = driver