import pandas as pd

matches = pd.read_csv('matches.csv')
players = pd.read_csv('players.csv')
stadiums = pd.read_json('stadiums.json')

#Añadir columna de nombre de ciudad a cada partido
matches['ciudad']=""

#Introducir nombre de ciudad según codigo de estadio 
for x in range((matches.shape[0])):
    for y in range((stadiums.shape[0])):
        if matches.iloc[x,5] == stadiums.iloc[y,0]:
            matches.iloc[x,5]= stadiums.iloc[y,2]
            
matches









print('Buenos dias entrenador, bienvenido a el tablero de resultados interactivo')