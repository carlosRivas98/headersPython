# Enviar información a través del encabezado
import requests

'''
query -> GET
cuerpo de la petición -> POST
encabezado 
'''

URL = "https://httpbin.org/post"

encabezado = {
    'curso': 'Matemáticas',
    'version': '2.0',
    'autor': 'Carlos Rivas'
}

params = {
    'plataforma': 'Prueba Online'
}

datos = {
    'usuario': 'Peter',
    'contraseña': '12345'
}


respuesta = requests.post(URL, headers=encabezado, params= params, data= datos)

if respuesta.status_code == 200:
     print(respuesta.text)