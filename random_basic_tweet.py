import datetime
from random import choice
from api_data import *
from autentificacion import autentificar
def random_basic_tweet(api, list):
    '''
    Esta funcion manda un tweet con el texto introducido

    Parámetros
    api: Objeto devuelto por <autentificar>
    list: Lista de strings con los tweets a enviar
    '''
    text = choice(list) 
    api.update_status(text)
    ahora = datetime.datetime.now()
    print(f"Tweet enviado: {text} a las {ahora}")

if __name__ == "__main__":
    tweets = ["000", "001", "002", "003"]
    api = autentificar(api_key, api_secret, access_token, access_secret)
    random_basic_tweet(api, tweets)