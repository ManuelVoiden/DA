#Nueva versión del conversor de monedas

import math
import json
from unittest import result
from urllib import request, response
import requests

print("Bienvenido a Monedapp 💰")
print("""Puedes convertir entre las siguientes monedas: 
-> EUR, USD, CAD, AUD, GBP, COP, CHF, MXN, ARS, CLP, PEN 
      """)
print("")
moneda_inicial = str(input('Que moneda quieres convertir: '))
moneda_final = str(input('A que moneda quieres convertir: '))
cantidad = int(input('Inserta el valor a convertir: '))
print("")

class conversor_moneda:
      rates: {}
      
      def __init__(self, url):
            data=requests.get(url).json()
            self.rates = data["rates"]
      
      def conversor(self, moneda_inicial, moneda_final, cantidad):
            cantidad_inicial = cantidad
            if moneda_inicial != 'EUR':
                  cantidad = cantidad/self.rates[moneda_inicial]
            print("Tu conversión está lista")
            print(f'{moneda_inicial} {cantidad_inicial} equivalen a {moneda_final} {cantidad}')
            
url = str.__add__('http://data.fixer.io/api/latest?access_key=','4e6b538d016ea8c6948fdf52ec855fbd')
c = conversor_moneda(url)
c.conversor(moneda_inicial, moneda_final, cantidad)
