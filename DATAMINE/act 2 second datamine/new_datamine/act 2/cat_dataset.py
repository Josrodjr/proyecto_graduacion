from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from googletrans import Translator

analyser = SentimentIntensityAnalyzer()
translator = Translator()

def score_neutrality(tweet):
    vader = analyser.polarity_scores(tweet)
    # print([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])
    # return pd.Series([vader['pos'], vader['neg'], vader['neu'], vader['compound']])
    return vader['neu']

def translate_tweet(tweet):
    result = translator.translate(tweet, dest='en')
    return result.text

def mainloop():
    # open the twees csv parseed
    df = pd.read_csv('tweets_parsed.csv')

    # generate a new dataframe only with the columns we will be using
    column_names = ["created_at", "text", "real_user"]
    result_df = pd.DataFrame(columns = column_names)

    # iterate over the rows of the first dataframe mining the user, createdat and text
    for index, row in df.iterrows():
        created_at = row['created_at']
        text =  row['text']
        real_user = row['real_user']

        # translate the text so can parse the neutrality
        text = translate_tweet(text)

        # get the neutrality in the text
        neutrality = score_neutrality(text)

        # if neutrality is between 1-0.75 not included in resulting dataframe
        if neutrality < 0.75:
            # insert into the real df
            result_df = result_df.append(pd.Series([created_at, text, real_user], index = result_df.columns), ignore_index=True)
        print(index)

    # after execution generate a new csv with values
    result_df.to_csv('sans_neutral.csv', index=None)


# text = 'This goes beyond party lines.  Separating families betrays our values as Texans, Americans and fellow human beings'
# text = 'Cosas que solo pasan el Colombia'
# text = translate_tweet(text)

mainloop()