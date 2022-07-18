from random import choice
import os

import tweepy

from api_data import *
from autentificacion import autentificar

def upload_random_media(api, img_path, text=""):
    
    '''
    Esta funcion manda una imagen y opcionalmente un texto

    api: Objeto devuelto por la funcion <autentificar>
    img_path: Ruta a la imagen, video o sonido que queremos twittear
    text: (Opcional) Mensaje a twittear
    '''
    media = api.media_upload(img_path)
    api.update_status(text, media_ids=[media.media_id_string])
    print("Tweet enviado")      

if __name__ == "__main__":
    img_path = "imgs/"
    files = os.listdir(img_path)
    target_img = choice(files)
    img_path += target_img
    print(img_path)
    api = autentificar(api_key, api_secret, access_token, access_secret)
    upload_random_media(api, img_path)