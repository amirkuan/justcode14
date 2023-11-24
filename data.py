import pandas as pd
import os

df = pd.read_csv('people.csv')

files = {'darina': 'Aidar.csv'}

dar = df[['Name', 'Age']]

if not os.path.exists('ata'):
    os.makedirs('ata')

dar.to_csv(os.path.join('ata.csv'), index=False)


