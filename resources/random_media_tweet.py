from random import choice
import os

import datetime

from api_data import *
from autentificacion import autentificar

def random_media_tweet(api, img_path, text=""):
    
    '''
    Esta funcion manda una imagen aleatoria de una carpeta y opcionalmente un texto

    api: Objeto devuelto por la funcion <autentificar>
    img_path: Ruta a la imagen, video o sonido que queremos twittear
    text: (Opcional) Mensaje a twittear
    '''
    files = os.listdir(img_path)
    target_img = choice(files)
    img = img_path+target_img
    media = api.media_upload(img)
    api.update_status(text, media_ids=[media.media_id_string])
    print(img)
    ahora = datetime.datetime.now()
    print(f"Tweet enviado: {text} a las {ahora}")      

if __name__ == "__main__":
    img_path = "imgs/"    
    api = autentificar(api_key, api_secret, access_token, access_secret)
    random_media_tweet(api, img_path)