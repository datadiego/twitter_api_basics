from random import choice
import os

import tweepy

from api_data import *

def upload_random_media(api_key, api_secret, access_token, access_secret, img_path, text=""):
    
    '''
    Esta funcion manda una imagen y opcionalmente un texto

    api_key: Token generado por twitter
    api_secret: Token generado por twitter
    access_token: Token generado por twitter
    access_secret: Token generado por twitter
    img_path: Ruta a la imagen, video o sonido que queremos twittear
    text: (Opcional) Mensaje a twittear
    '''
    try:
        auth = tweepy.OAuthHandler(api_key,api_secret)
        auth.set_access_token(access_token,access_secret)
        api = tweepy.API(auth)
        api.verify_credentials()
        print('Autentificacion exitosa')
    except:
        print('Autentificacion de credencialles fallida')
    media = api.media_upload(img_path)
    api.update_status(text, media_ids=[media.media_id_string])
    print("Tweet enviado")      

if __name__ == "__main__":
    img_path = "imgs/"
    files = os.listdir(img_path)
    target_img = choice(files)
    img_path += target_img
    print(img_path)
    upload_random_media(api_key, api_secret, access_token, access_secret, img_path)