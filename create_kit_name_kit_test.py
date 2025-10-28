import sender_stand_request
import data


# ---------- FUNCIONES AUXILIARES ----------

def get_kit_body(name):
    """Devuelve una copia del cuerpo base del kit, cambiando solo el campo 'name'."""
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_new_user(user_body)

    # Imprime el código de estado y el cuerpo de la respuesta para depurar
    print(f"Código de estado: {response.status_code}")
    print(f"Cuerpo de la respuesta: {response.text}")

    # Intenta acceder al authToken solo si la respuesta fue exitosa
    if response.status_code == 201:  # 201 Created es un código de éxito común para crear recursos
        return response.json()["authToken"]
    else:
        # En caso de error, puedes manejarlo o lanzar una excepción más clara
        raise Exception(
            f"Fallo al obtener el token. Código de estado: {response.status_code}, Respuesta: {response.text}")


def positive_assert(kit_body):
    """Verifica que el kit se cree correctamente con código 201 y el nombre coincida."""
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201, f"Error: se esperaba 201, se obtuvo {response.status_code}"
    assert response.json()["name"] == kit_body["name"], "El campo 'name' no coincide"


def negative_assert_code_400(kit_body):
    """Verifica que el código de respuesta sea 400 (solicitud inválida)."""
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400, f"Error: se esperaba 400, se obtuvo {response.status_code}"


# ---------- LISTA DE VERIFICACIÓN DE PRUEBAS ----------

# 1️⃣ Número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# 2️⃣ Número permitido de caracteres (511)
def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body("a" * 511)
    positive_assert(kit_body)


# 3️⃣ Número de caracteres menor al permitido (0)
def test_create_kit_0_letters_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# 4️⃣ Número de caracteres mayor al permitido (512)
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("a" * 512)
    negative_assert_code_400(kit_body)


# 5️⃣ Se permiten caracteres especiales
def test_create_kit_special_characters_in_name_get_success_response():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)


# 6️⃣ Se permiten espacios
def test_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# 7️⃣ Se permiten números
def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# 8️⃣ El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


# 9️⃣ Tipo de parámetro diferente (número)
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)


