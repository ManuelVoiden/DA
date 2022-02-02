#Nueva versión del conversor de monedas

import math
import json
from unittest import result
from urllib import request, response
import requests
class conversor_moneda:
      rates: {}
      
      def __init__(self, url):
            data=requests.get(url).json()
            self.rates = data["rates"]
      
      def conversor(self, moneda_inicial, moneda_final, cantidad):
            cantidad_inicial = cantidad
            if moneda_inicial == 'EUR':
                  cantidad = cantidad*self.rates[moneda_final]
            elif moneda_inicial != 'EUR': 
                  cantidad = ((cantidad/self.rates[moneda_inicial])*self.rates[moneda_final])
            print("Tu conversión está lista")
            print(f'{moneda_inicial} {"{:,.2f}".format(cantidad_inicial)} equivalen a {moneda_final} {"{:,.2f}".format(cantidad)}')
            
if __name__ == "__main__":
      url = str.__add__('http://data.fixer.io/api/latest?access_key=','4e6b538d016ea8c6948fdf52ec855fbd')
      c = conversor_moneda(url)
      
      print("")
      print("Bienvenido a Monedapp 💰")
      print("""Puedes convertir entre las siguientes monedas: 
 -> EUR, USD, CAD, AUD, GBP, COP, CHF, MXN, ARS, CLP, PEN 
      """)
      
      moneda_inicial = str(input('Que moneda quieres convertir: '))
      moneda_inicial = moneda_inicial.upper()
      moneda_final = str(input('A que moneda quieres convertir: '))
      moneda_final = moneda_final.upper()
      cantidad = int(input('Inserta el valor a convertir: '))
      
      print("")
      
      c.conversor(moneda_inicial, moneda_final, cantidad)
