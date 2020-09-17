import pandas as pd

# open the twees csv parseed
df = pd.read_csv('sans_neutral.csv')

for index, row in df.iterrows():
    print(index)