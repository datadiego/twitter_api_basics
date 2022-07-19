from api_data import api_key, api_secret, access_token, access_secret
from autentificacion import autentificar
import tweepy

class Tweet_bot:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.client = self.autentificar(self.api_key, self.api_secret, self.access_token, self.access_secret)
        self.client.verify_credentials()
        self.twitter_user = self.client.get_user(screen_name="infolepsy20k")
        self.id = self.twitter_user.id
        self.name = self.twitter_user.name
        self.texts_to_send = []
        self.muestra_info()

    def add_texts(self, list):
        for element in list:
            self.texts_to_send.append(element)
    
    def muestra_info(self):
        print(f"Sesión iniciada como @{self.name}\nID de usuario: {self.id}")    
    
    def autentificar(self, api_key, api_secret, access_token, access_secret):
        """
        Esta funcion verifica tus credenciales en la API de twitter.

        Parámetros:
        api_key: Token proporcionado por twitter
        api_secret: Token proporcionado por twitter
        access_token: Token proporcionado por twitter
        access_secret: Token propocionado por twitter
        """
        try:
            auth = tweepy.OAuthHandler(api_key, api_secret)
            auth.set_access_token(access_token, access_secret)
            api = tweepy.API(auth)
            api.verify_credentials()
            print('Autentificación exitosa')
            return api     
        except Exception as error:
            print(f'Autentificación fallida {error}')

    def get_last_tweet(self):
        tweet = self.client.user_timeline(count = 1)[0]
        print(f"Último tweet enviado: {tweet.text}")
        return tweet.text

    def get_last_tweet_id(self):
        tweet = self.client.user_timeline(count = 1)[0]
        print(f"ID del último tweet enviado: {tweet.id}")
        return tweet.id
    
    def delete_last_tweet(self):
        last_tweet_id = self.get_last_tweet_id()
        self.client.destroy_status(last_tweet_id)
        print("Ultimo tweet eliminado")
    
    def get_tweets(self, amount):
        count = 0
        last_tweets = []
        while count < amount:
            tweet = self.client.user_timeline(count=count+1)[count]
            last_tweets.append(tweet.text)
            count += 1
        print(f"Ultimos {amount} tweets:")
        print(last_tweets)
        return last_tweets

    def get_tweets_id(self, amount):
        count = 0
        last_tweets = []
        while count < amount:
            tweet = self.client.user_timeline(count=count+1)[count]
            last_tweets.append(tweet.id)
            count += 1
        print(f"ID's de los ultimos {amount} tweets:")
        print(last_tweets)
        return last_tweets


if __name__ == "__main__":
    bot = Tweet_bot(api_key, api_secret, access_token, access_secret)
    bot.get_tweets(3)