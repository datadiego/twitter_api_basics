from api_data import *
import tweepy

def autentificar(api_key, api_secret, access_token, access_secret):
    """
    Esta funcion verifica tus credenciales en la API de twitter.

    Parámetros:
    api_key: Token proporcionado por twitter
    api_secret: Token proporcionado por twitter
    access_token: Token proporcionado por twitter
    access_secret: Token propocionado por twitter
    """
    try:
        #Autentificar con la api de twitter:
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        api.verify_credentials()
        print('Autentificación exitosa')
        return api     
    except:
        print('Autentificación fallida')

if __name__ == "__main__":
    autentificar(api_key, api_secret, access_token, access_secret)
