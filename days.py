def top(tweets):
    tweets['date'] = tweets['date'].dt.date
    top_days = tweets['date'].value_counts()
    return top_days