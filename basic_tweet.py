import tweepy, datetime
from api_data import *

def create_tweet(api_key, api_secret, access_token, access_secret, text):
    '''
    Esta funcion manda un tweet con el texto introducido

    Parámetros
    text: Mensaje a twittear
    api_key: Token generado por twitter
    api_secret: Token generado por twitter
    access_token: Token generado por twitter
    access_secret: Token generado por twitter
    '''
    try:
        #Autentificar con la api de twitter:
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        api.verify_credentials()
        print('Autentificación exitosa')       
    except:
        print('Autentificación fallida')
    
    #Mandar tweet
    api.update_status(text)
    ahora = datetime.datetime.now()
    print(f"Tweet: {text}, enviado a las {ahora}")

if __name__ == "__main__":
    create_tweet("TEST", api_key, api_secret, access_token, access_secret)