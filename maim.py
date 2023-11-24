import pandas as pd
import os

df = pd.read_csv('people.csv')

files = {30: '30.csv'}

for key, value in files.items():
    filtered_df = df[df['Age'] >= key]
    print(filtered_df)
    if not os.path.exists('ta'):
        os.makedirs('ta')

    filtered_df.to_csv(os.path.join('ta', value), index=False)
