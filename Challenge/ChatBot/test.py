import pandas as pd

matches = pd.read_csv(r'matches.csv')
import csv 
file= open('matches.csv')
rows=[]
csvreader= csv.reader(file)
for row in csvreader:
    print(row)
    
    
for i in range(10):
    print(i)