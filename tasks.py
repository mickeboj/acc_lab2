from __future__ import absolute_import, unicode_literals
from .capp import app
import json


def tweet_clean(tweet):
        tweet = tweet.replace(".","")
        tweet = tweet.replace(",","")
        tweet = tweet.replace("!","")
        tweet = tweet.replace("?","")
        tweet = tweet.replace(":","")
        tweet = tweet.replace(";","")
        return tweet

@app.task
def count_file(fn,w_count,words):
    fd = open("tweets/"+fn)
    str_l = fd.read().split("\n\n")
    str_l.pop()
    for str_e in str_l:
            tweet = json.loads(str_e)["text"]
            if tweet.split()[0]=="RT":
                continue
            w_count["unique_tweets"] = w_count.get("unique_tweets",0) + 1
            tweet = tweet_clean(tweet.lower())
            for word in tweet.split():
                    if word in words:
                            w_count[word.encode('ascii','ignore')] = w_count.get(word, 0) + 1
    return w_count

if __name__== "__main__":
    words  = ["han","hon","hen","den","det","denne","denna"]
    w_count = {}
    print count_file("05cb5036-2170-401b-947d-68f9191b21c6",w_count,words)
