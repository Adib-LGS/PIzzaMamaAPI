import requests
import  json

url = 'http://127.0.0.1:8000/api/GetPizza'

data = requests.get(url)
# print(data.text)

pizzas = json.loads(data.text)
print(pizzas)
print(len(pizzas))

# Show pizza's names
for pizza in pizzas:
    pizzaModel = pizza['fields']
    print(pizzaModel)

# Press "RUN" to see serialize data in venv console
