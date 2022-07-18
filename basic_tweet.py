import datetime
from api_data import *
from autentificacion import autentificar

def create_tweet(api, text):
    '''
    Esta funcion manda un tweet con el texto introducido

    Parámetros
    api: Objeto devuelto por la funcion <autentificar>
    text: Mensaje a mandar
    '''
    api.update_status(text)
    ahora = datetime.datetime.now()
    print(f"Tweet: {text}, enviado a las {ahora}")

if __name__ == "__main__":
    api = autentificar(api_key, api_secret, access_token, access_secret)
    create_tweet(api, ":)")