import pandas as pd

def top(tweets):
    list_hashtag = []
    for msg in tweets['renderedContent']:
        frase = ''
        hashtag = False
        for letter in msg:
            if letter == '#':
                hashtag = True
                frase = ''
            if letter == ' ':
                hashtag = False
                list_hashtag.append(frase)
            if hashtag:
                frase += letter
    top_hashtag = pd.DataFrame(list_hashtag, columns = ['frase'])
    top_hashtag = top_hashtag['frase'].value_counts()
    return top_hashtag
    
