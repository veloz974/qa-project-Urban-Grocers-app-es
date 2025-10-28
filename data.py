import random

# Headers
headers = {
    "Content-Type": "application/json"
}

# Genera un número de teléfono aleatorio con el formato requerido.
def generate_random_phone_number():
    """Genera un número de teléfono aleatorio con un prefijo y 10 dígitos."""
    # Puedes ajustar el prefijo y la cantidad de dígitos si es necesario
    prefix = "+1"
    random_digits = ''.join(random.choices('0123456789', k=10))
    return f"{prefix}{random_digits}"

# Cuerpo del usuario con un número de teléfono que se genera dinámicamente.
user_body = {
    "firstName": "Ariana",
    "phone": generate_random_phone_number(),
    "address": "123 Elm Street, Hilltop"
}

# Cuerpo base del kit (se modificará dinámicamente en las pruebas)
kit_body = {
    "name": "a"
}




