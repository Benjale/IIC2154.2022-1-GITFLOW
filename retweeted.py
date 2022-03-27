def top(tweets):
    most_retweeted = tweets.sort_values('retweetCount', ascending=False)
    return most_retweeted