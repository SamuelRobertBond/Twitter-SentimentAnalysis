import sqlite3
import re
import time

database_name = "TweetDB.db"
table_name = "TwitterInformation"
column_1 = "SearchType"
column_2 = "SearchTerm"
column_4 = "Tweet"
pattern = re.compile('([^\s\w]_)+')


def record_tweets(tweet_type, term, tweets):
    tweet_type = str(tweet_type)
    term = str(term)

    try:
        con = sqlite3.connect(database_name)
        cur = con.cursor()

        for tweet in tweets:
            tweet_text = pattern.sub('', tweet.text)
            tweet_text = tweet_text.replace("\"", '""')

            cur.execute('INSERT INTO {tn} VALUES ("{v1}","{v2}","{v3}","{v4}")'.
                        format(tn=table_name, v1=tweet_type, v2=term, v3=time.strftime("%x"), v4=tweet_text))

        con.commit()
        con.close()
        print("done")
        return
    except sqlite3.OperationalError as e:
        print(tweet_text)
        print(e.message)
        print("Failed")
    return


def retrieve_tweets_by_term(query):

    print("Retrieving")

    term = str(query)
    con = sqlite3.connect(database_name)
    cur = con.cursor()

    cur.execute('SELECT {coi1} FROM {tn} WHERE {coi2}={tm}'.
                format(coi1=column_4, tn=table_name, coi2=column_2, tm='"' + term + '"'))

    table_data = cur.fetchall()

    for x in range(0, len(table_data)):
        print("".join(table_data[x]))

    return table_data
