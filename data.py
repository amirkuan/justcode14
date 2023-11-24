import pandas as pd
import os

df = pd.read_csv('people.csv')

darina = df[['Name', 'Age']]
print(darina)