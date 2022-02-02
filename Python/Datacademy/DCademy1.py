#Nueva versión del conversor de monedas

import math
import json
from unittest import result
from urllib import response
import requests

print("Bienvenido a monedapp")
print("""Puedes convertir entre las siguientes monedas: 
-> EUR, USD, CAD, AUD, GBP, COP, CHF, MXN, ARS, CLP, PEN 
      """)
print("")
moneda_inicio = str(input('Que moneda quieres convertir: '))
moneda_final = str(input('A que moneda quieres convertir: '))
cantidad = int(input('Inserta el valor a convertir: '))
print("")


response = requests.get(f'https://api.exchangeratesapi.io/v1/latest?base={moneda_inicio}&symbols={moneda_final}')
data = response.json()
tasa_de_cambio = data['rates'][moneda_inicio]
resultado = cantidad*tasa_de_cambio
print("Tu conversión está lista")
print(f'{moneda_inicio} {cantidad} equivalen a {moneda_final} {tasa_de_cambio}')