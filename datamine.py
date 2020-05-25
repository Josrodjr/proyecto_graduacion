import json
from tweepy import StreamListener, OAuthHandler, Stream
from textblob import TextBlob

credentials = {}
credentials['CONSUMER_KEY'] = "NFYbz1LOrf1yPt2gE2StszCJ1"
credentials['CONSUMER_SECRET'] = "MbiuwBgXFSmuC9M6u4m3BKNSkw1512bIg4DNpmUbBt5NGmW1jw"
credentials['ACCESS_TOKEN'] = "1251725870772957186-zvQFhOKbYJv6IbvfA2kS4hLyAogTwg"
credentials['ACCESS_SECRET'] = "ZL2Ok63GOf7U90D2Alb3bqjKd0qZBeUazALhMmrppX7Qf"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)

#Basic Listener
class StdOutListener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = TextBlob(all_data["text"])

        #Add the 'sentiment data to all_data
        # all_data['sentiment'] = tweet.sentiment

        #print(tweet)
        #print(tweet.sentiment)

        # Open json text file to save the tweets
        with open('tweets.json', 'a') as tf:
            # Write a new line
            tf.write('\n')

            # Write the json data directly to the file
            json.dump(all_data, tf)
            # Alternatively: tf.write(json.dumps(all_data))
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
    auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'])
    # Start a stream of data
    stream = Stream(auth, l)

    # # Check for data using the params in track
    # stream.filter(languages = ['en'], track=['UniversalStudios Disneyland LosAngeles'])

    file = open("depression_related_keywords.txt", "r")
    track_criteria = []
    for value in file:
        treated_value = value.strip()
        track_criteria.append(treated_value)

    stream.filter(languages = ['es'], track=track_criteria)

    # referencias
    # https://stackoverflow.com/questions/49027297/how-to-get-tweets-data-that-contain-multiple-keywords
    # https://stackoverflow.com/questions/22456274/how-to-completely-remove-n-in-text-file-using-python
    # https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters
    # https://stackabuse.com/accessing-the-twitter-api-with-python/