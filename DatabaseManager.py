import sqlite3

database_name = "TweetDB.db"
table_name = "TwitterInformation"
column_1 = "SearchType"
column_2 = "SearchTerm"
column_3 = "Tweet"


def record_tweet(tweet_type, term, tweet):
    tweet_type = str(tweet_type)
    term = str(term)
    tweet = str(tweet)

    con = sqlite3.connect(database_name)
    cur = con.cursor()

    cur.execute('INSERT INTO {tn} VALUES ("{v1}","{v2}","{v3}")'.
                format(tn=table_name, v1=tweet_type, v2=term, v3=tweet))

    con.commit()
    print("done")
    return


def retrieve_tweets_by_term(query):

    print("Retrieving")

    term = str(query)
    con = sqlite3.connect(database_name)
    cur = con.cursor()

    cur.execute('SELECT {coi1} FROM {tn} WHERE {coi2}={tm}'.
                format(coi1=column_3, tn=table_name, coi2=column_2, tm='"' + term + '"'))

    table_data = cur.fetchall()

    for x in range(0, len(table_data)):
        print("".join(table_data[x]))

    return table_data


