from api_data import *
from autentificacion import autentificar

def media_tweet(api, img_path, text=""):
    
    '''
    Esta funcion manda una imagen y opcionalmente un texto

    api = Objeto devuelto por la funcion <autentificar>
    img_path: Ruta a la imagen, video o sonido que queremos twittear
    text: (Opcional) Mensaje a twittear
    '''
    media = api.media_upload(img_path)
    api.update_status(text, media_ids=[media.media_id_string])
    print("Tweet enviado")      

if __name__ == "__main__":
    api = autentificar(api_key, api_secret, access_token, access_secret)
    media_tweet(api, "imgs/img_0.png", "TEST")