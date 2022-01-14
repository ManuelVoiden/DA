import math

eur_usd = 1.13
usd_eur = 0.88
eur_cop = 4603.37
cop_eur = 0.00022
usd_cop = 4070
cop_usd = 0.00025

mon1 = 'EUR' 
mon2 = 'USD' 
mon3 = 'COP'

valor_a_convertir = 0
valor_final = 0

print("Bienvenido a monedapp")
print("Puedes convertir entre las siguientes monedas: EUR, USD y COP")
print("")
moneda_inicio = str(input('Que moneda quieres convertir: '))
moneda_final = str(input('A que moneda quieres convertir: '))
print("")

if moneda_inicio == mon1 and moneda_final == mon2:
    print(f'Convertiremos entre {mon1} y {mon2}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * eur_usd
    print(f'{mon1} {valor_a_convertir} equivale a {mon2} {valor_final}')
elif moneda_inicio == mon1 and moneda_final == mon3:
    print(f'Convertiremos entre {mon1} y {mon3}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * eur_cop
    print(f'{mon1} {valor_a_convertir} equivale a {mon3} {valor_final}')
elif moneda_inicio == mon2 and moneda_final == mon3:
    print(f'Convertiremos entre {mon2} y {mon3}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * usd_cop
    print(f'{mon2} {valor_a_convertir} equivale a {mon3} {valor_final}')
elif moneda_inicio == mon2 and moneda_final == mon1:
    print(f'Convertiremos entre {mon2} y {mon1}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * usd_eur
    print(f'{mon2} {valor_a_convertir} equivale a {mon1} {valor_final}')
elif moneda_inicio == mon3 and moneda_final == mon1:
    print(f'Convertiremos entre {mon3} y {mon1}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * cop_eur
    print(f'{mon3} {valor_a_convertir} equivale a {mon1} {valor_final}')
elif moneda_inicio == mon3 and moneda_final == mon2:
    print(f'Convertiremos entre {mon3} y {mon2}')
    valor_a_convertir = float(input('Inserta el valor a convertir: '))
    valor_final = valor_a_convertir * cop_usd
    print(f'{mon3} {valor_a_convertir} equivale a {mon2} {valor_final}')
else:
    print('******************************************')
    print('ERROR, moneda no soportada por el programa')
    print('******************************************')    

print("")
print('¡Gracias por usar Monedapp!')
    
    
    
