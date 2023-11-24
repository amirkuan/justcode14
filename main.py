import pandas as pd
import os

df = pd.read_csv('people.csv')

files = {'Male': 'male_data.csv', 'Female': 'female_data.csv'}

for key, value in files.items():
    filtered_df = df[df['Gender'] == key]
    print(filtered_df)
    if not os.path.exists('filtered_data'):
        os.makedirs('filtered_data')

    filtered_df.to_csv(os.path.join('filtered_data', value), index=False)
