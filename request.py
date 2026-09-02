import requests

url = "https://e36a-152-203-184-176.ngrok-free.app"

# Este header evita la pantalla de advertencia 'ngrok-skip-browser-warning'
headers = {
    "ngrok-skip-browser-warning": "true",
    "User-Agent": "MyPythonScript/1.0"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    print(f"Código de estado: {response.status_code}\n")
    print("Respuesta:")
    print(response.text)

except requests.exceptions.RequestException as error:
    print(f"Error en la petición: {error}")
