import datetime
from authentication import api
import random

last_response = api.user_timeline(screen_name = '@GospelofKanye', count=1) #returns a list of recent statuses
most_recent_status_id = last_response[0].id
most_recent_kanye_tweets = api.user_timeline(screen_name = '@kanyewest') #pull most recent 20 tweets from kanye's twitter feed
for tweet in most_recent_kanye_tweets:
    kanye_tweet_id = tweet.id
    if kanye_tweet_id > most_recent_status_id:
        single_tweet = tweet.text # extract tweet text only
        if 'https' not in single_tweet: #filter out tweets of images, videos, links, etc.
            chapter = str(random.randint(1,51)) #randomly generate a fake bible chapter number
            verse = str(random.randint(1,26)) #randomly generate a fake verse number
            message = ' Kanye ' + chapter + ':' + verse + ' ' + single_tweet #create a new message with the text, plus "Kanye chapter:verse"
            print(message)

api.update_status(message) 
