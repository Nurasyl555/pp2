import json 
# some JSON
# Если у вас есть строка JSON, вы можете проанализировать ее с помощью метода json.loads().
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y['age'])
print(type(y))