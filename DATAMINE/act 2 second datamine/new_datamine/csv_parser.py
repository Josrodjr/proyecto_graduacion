import pandas

df = pandas.read_json('tweets.json', lines=True)
df.to_csv('tweets.csv', index=None)

