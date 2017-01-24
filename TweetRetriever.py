import DatabaseManager
import tweepy

# Credit to this solution on Stack Overflow which helped me figure out searching with Tweepy
# http://stackoverflow.com/questions/22469713/managing-tweepy-api-search


def mine_tweets(search_term):
    consumer_key = "c1txbSNlGU5CzquT2lQyY8yLX"
    consumer_secret_key = "SImAc0YrnR1WVp09aU4iRT3X24CGhz8P5okLA8quEKpK7xYgbO"
    access_token = "821903005389824000-Zg0ACXTDvsEGzasC6rJWjueLpwXVQJh"
    access_token_secret = "w6S8YVlGLntzjeQAmqGVsu2uEkm958o5JqVELpAECA1xK"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    max_tweets = 1000
    tweets = []
    last_id = -1

    while len(tweets) < max_tweets:
        try:
            count = max_tweets - len(tweets)
            new_tweets = api.search(q=search_term, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print(e.message)
            break

    DatabaseManager.record_tweets("String", search_term, tweets)

    return
