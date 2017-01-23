import DatabaseManager
import tweepy

consumer_key = "c1txbSNlGU5CzquT2lQyY8yLX"
consumer_secret_key = "SImAc0YrnR1WVp09aU4iRT3X24CGhz8P5okLA8quEKpK7xYgbO"
access_token = "821903005389824000-Zg0ACXTDvsEGzasC6rJWjueLpwXVQJh"
access_token_secret = "w6S8YVlGLntzjeQAmqGVsu2uEkm958o5JqVELpAECA1xK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

