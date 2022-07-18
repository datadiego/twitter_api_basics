from api_data import *
import tweepy

def autentificar(api_key, api_secret, access_token, access_secret):
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