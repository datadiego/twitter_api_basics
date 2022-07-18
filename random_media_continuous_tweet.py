import datetime, os, time
from random import choice

from api_data import *

from autentificacion import autentificar

def upload_cont_random_media(api, minutes, img_path, text=""):
    '''
    Esta funcion manda imagenes y opcionalmente un texto de manera periódica, ajusta el tiempo entre tweets mediante el parametro "minutes"

    api: Objeto devuelto por <autentificar>
    minutes: Minutos a esperar entre tweets
    img_path: Ruta a la imagen, video o sonido que queremos twittear
    text: (Opcional) Mensaje a twittear
    '''
    minutes *= 60
    files = os.listdir(img_path)
    while True:
        target_img = choice(files)
        img = img_path+target_img
        media = api.media_upload(img)
        api.update_status(text, media_ids=[media.media_id_string])
        ahora = datetime.datetime.now()
        print(f"Tweet enviado: {text} a las {ahora}")
        time.sleep(minutes)
        

if __name__ == "__main__":
    img_path = "imgs/"
    api = autentificar(api_key, api_secret, access_token, access_secret)
    upload_cont_random_media(api, 2, img_path)