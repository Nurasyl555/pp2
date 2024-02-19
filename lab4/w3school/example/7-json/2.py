import json
# Если у вас есть объект Python, вы можете преобразовать его в строку JSON с помощью метода json.dumps()
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON
y = json.dumps(x)
print(y)
print(type(y))