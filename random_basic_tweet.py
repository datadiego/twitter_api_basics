import tweepy, datetime
from random import choice
from api_data import *
from autentificacion import autentificar
def create_tweet(api_key, api_secret, access_token, access_secret, list):
    '''
    Esta funcion manda un tweet con el texto introducido

    Parámetros
    text: Mensaje a twittear
    api_key: Token generado por twitter
    api_secret: Token generado por twitter
    access_token: Token generado por twitter
    access_secret: Token generado por twitter
    '''
    text = choice(list)
    api = autentificar(api_key, api_secret, access_token, access_secret)
    #Mandar tweet
    api.update_status(text)
    ahora = datetime.datetime.now()
    print("Tweet enviado a las", ahora)

if __name__ == "__main__":
    tweets = ["000", "001", "002", "003"]
    create_tweet(api_key, api_secret, access_token, access_secret, tweets)