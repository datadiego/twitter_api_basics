import tweepy

def peticion(text):
    resultado = ""
    while resultado == "":
        resultado = input(text)
    return resultado
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
    except Exception as error:
        print(f'Autentificación fallida {error}')
print("\n######### Configuración de api_data.py #########")
print("Vamos a configurar tus credenciales.\nPuedes encontrar una guía sobre como obtener tus keys en: ")
print("https://github.com/datadiego/twitter_api_basics")
api_key = peticion("Ingresa tu API Key: ")
api_secret = peticion("Ingresa tu API Secret Key: ")
access_token = peticion("Ingresa tu Access Token: ")
access_secret = peticion("Ingresa tu Access Secret Token: ")

test_autentificacion = ""
while test_autentificacion != "y" and test_autentificacion !="n":
    test_autentificacion = peticion("¿Testear credenciales? (y/n) ")
    test_autentificacion = test_autentificacion.lower()

if test_autentificacion == "y":
    print("Intentando autentificar: ")
    autentificar(api_key, api_secret, access_token, access_secret)


keys = {"api_key":api_key, "api_secret":api_secret, "access_token":access_token, "access_secret":access_secret}
sav = ""
while sav != "y" and sav != "n":
    sav = peticion("¿Guardar y crear archivo api_data.py? Esto sobreescribirá las keys anteriores (y/n) ")
if sav == "y":
    file_name = "api_data.py"
    with open("resources/"+file_name, "w") as file:
        for data in keys:
            file.write(data+" = '"+keys[data]+"'\n")
else:
    print("El archivo api_data.py no se escribió")
print("Instalación terminada")
