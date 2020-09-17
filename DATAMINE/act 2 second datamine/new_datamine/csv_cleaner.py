import pandas
import json
import ast

# open the values found in the csv
df = pandas.read_csv('tweets.csv')

# generate a new dataframe only with the columns we will be using
column_names = ["created_at", "text", "real_user"]
real_df = pandas.DataFrame(columns = column_names)

# iterate over the rows of the first dataframe mining the user, createdat and text
for index, row in df.iterrows():
    created_at = row['created_at']
    text =  row['text']

    # parse the user
    # json_user = json.loads(row['user'])
    long_user = row['user']
    user_dict = ast.literal_eval(long_user)
    real_user = user_dict['screen_name']

    # insert into the real df
    # real_df = pandas.concat([real_df, pandas.Series([created_at, text, real_user])])
    real_df = real_df.append(pandas.Series([created_at, text, real_user], index = real_df.columns), ignore_index=True)


# after execution generate a new csv with values
real_df.to_csv('tweets_parsed.csv', index=None)
