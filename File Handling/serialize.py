import json

data = {
  "name":"bhushan",
  "age":32,
  "city":"Goa"
}

json_data = json.dumps(data)
print(type(json_data))
print(json_data)

#deserialize
user  = json.loads(json_data)
print(user)
print(type(user))