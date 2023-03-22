def obtener_tweets_autor(lista_tweets, autor):
    tweets_autor = []
    for tweet in lista_tweets:
        if tweet["autor"].lower() == autor.lower():
            tweets_autor.append(tweet)
    return tweets_autor


tweets = [{"tweet": "Me gusta el queso", "autor": "Ana"}]
tweets_autor = obtener_tweets_autor(lista_tweets=tweets, autor="Ana")
