# Proyecto Urban Grocers 

En este este proyecto automatiza las pruebas de creación de kits y usuarios utilizando la API de Urban Grocers.

El objetivo del proyecto es verificar la funcionalidad en la creación de kits así como la verificación de otros endpoints.
## Archivos principales:
- `configuration.py`: Configuraciones generales (URLs, endpoints).
- `data.py`: Datos de prueba.
- `sender_stand_request.py`: Envío de solicitudes HTTP.
- `create_kit_name_kit_test.py`: Pruebas automatizadas con pytest.
- .gitignore

Ejecución de pruebas 
## Cómo ejecutar las pruebas:
```bash
pytest create_kit_name_kit_test.py test -v
