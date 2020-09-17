import pandas as pd
# twitter management
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import TweepError
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys


# open the twees csv parseed
# df = pd.read_csv('sans_neutral.csv')

# generate a list with the complete users tagged
account_list = ['guatemalaglobal']
err_count = 0

# # iterate over the rows
# for index, row in df.iterrows():
#     created_at = row['created_at']
#     text =  row['text']
#     real_user = row['real_user']

#     account_list.append(real_user)

# print the result
# print(account_list)

# twitter suff
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

# generate a new dataframe only with the columns we will be using
column_names = ["name", "twitter_username", "twitter_description", "tweets_number", "friends_number", "followers_number", "account_age_days", "tweets_per_day", "most_used_hashtags", "tweets_list"]
final_df = pd.DataFrame(columns = column_names)

if len(account_list) > 0:
  for target in account_list:
      # print("Getting data for " + target)
    try:
        item = auth_api.get_user(target)
        print(item)
        name = item.name
        twitter_username = item.screen_name
        twitter_description = item.description
        tweets_number = str(item.statuses_count)
        friends_number = str(item.friends_count)
        followers_number = str(item.followers_count)

        tweets = item.statuses_count
        account_created_date = item.created_at
        delta = datetime.utcnow() - account_created_date
        account_age_days = delta.days
        # print("Account age (in days): " + str(account_age_days))
        tweets_per_day = 0
        if account_age_days > 0:
            tweets_per_day = "%.2f"%(float(tweets)/float(account_age_days))

        hashtags = []
        tweets_list = []
        tweet_count = 0
        end_date = datetime.utcnow() - timedelta(days=3000)
        for status in Cursor(auth_api.user_timeline, id=target).items():
            tweet_count += 1
            if hasattr(status, "text"):
                tweets_list.append(status.text)
            if hasattr(status, "entities"):
                entities = status.entities
                if "hashtags" in entities:
                    for ent in entities["hashtags"]:
                        if ent is not None:
                            if "text" in ent:
                                hashtag = ent["text"]
                                if hashtag is not None:
                                    hashtags.append(hashtag)
            if status.created_at < end_date:
                break

        # print("Most used hashtags:")
        # for item, count in Counter(hashtags).most_common(10):
        #   print(item + "\t" + str(count))
        most_used_hashtags = hashtags

        # print( "All done. Processed " + str(tweet_count) + " tweets.")
        print("Processed " + str(target))

        # insert into the row the resulting data
        final_df = final_df.append(pd.Series([name, twitter_username, twitter_description, tweets_number, friends_number, followers_number, account_age_days, tweets_per_day, most_used_hashtags, tweets_list], index = final_df.columns), ignore_index=True)
    
    except:
        print("error no" + str(err_count))
        err_count += 1

final_df.to_csv('testt.csv', index=None)