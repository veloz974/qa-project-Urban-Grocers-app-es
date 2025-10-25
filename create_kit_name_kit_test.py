
import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import user_body, kit_test_data


@pytest.fixture(scope="session")
def auth_token():
    """Crea un usuario y devuelve su token de autenticación."""
    response = post_new_user(user_body)
    assert response.status_code == 201, "Error al crear usuario"
    return response.json()["authToken"]


def test_create_kit_name(auth_token):
    """Ejecuta todas las pruebas definidas en la checklist."""
    for case in kit_test_data:
        response = post_new_client_kit(case, auth_token)
        name = case.get("name")

        # ✅ Casos válidos
        if isinstance(name, str) and 1 <= len(name) <= 511:
            assert response.status_code == 201, f"Fallo con name={name}"
            assert response.json()["name"] == name, "El nombre no coincide"

        # ❌ Casos inválidos
        else:
            assert response.status_code == 400, f"Fallo con name={name}"


