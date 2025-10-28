import requests
import data
import configuration

#### Función para crear un usuario
def post_new_user(body):
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

#### Función para crear un kit asociado al usuario
def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    return requests.post(
        configuration.BASE_URL + configuration.KITS_PATH,
        json=kit_body,
        headers=headers_dict
    )
