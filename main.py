import requests

url = 'http://127.0.0.1:8000/api/GetPizza'

data = requests.get(url)
print(data.text)


# Press "RUN" to see serialize data in venv console
