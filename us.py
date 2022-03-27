def top(tweets, dfNew, users):
    most_active_user = tweets['userId'].value_counts()
    for id_user in most_active_user.head(10).index:
        fila = users[users['userId'] == id_user]
        fila = fila[['username', 'displayname', 'userId']]
        dfNew=dfNew.append(fila,ignore_index=True)
    return dfNew