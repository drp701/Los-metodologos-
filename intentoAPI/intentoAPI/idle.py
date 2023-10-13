import requests

# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingrese el valor de n para Fibonacci: "))

# Hacer la solicitud a la API local
url = f"http://127.0.0.1:5000/fibonacci/{n}"
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el resultado en formato JSON
    result = response.json()
    
    # Mostrar el resultado
    print(f"El {n}-ésimo término de la secuencia de Fibonacci es: {result['fibonacci']}")
else:
    # Mostrar un mensaje de error si la solicitud no fue exitosa
    print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")