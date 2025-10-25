
import requests
from configuration import BASE_URL, CREATE_USER_PATH, KITS_PATH, TIMEOUT


def post_new_user(body):
    """Crea un nuevo usuario y devuelve la respuesta completa."""
    url = BASE_URL + CREATE_USER_PATH
    response = requests.post(url, json=body, timeout=TIMEOUT)
    return response


def post_new_client_kit(kit_body, auth_token):
    """Crea un nuevo kit para un usuario usando su token."""
    url = BASE_URL + KITS_PATH
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(url, headers=headers, json=kit_body, timeout=TIMEOUT)
    return response

