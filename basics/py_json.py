# JSON is commonly used with data APIS
# here is how we can parse JSON into a python dictionary

import json

# Sample JSON
userJSON = '{"first_name":"john","last_name":"doe","age":30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# Cannot name is json.py due to conflict with the module

# turn to json

car = {'make': "ford", "model": "mustang", "year": 1970}

carJSON = json.dumps(car)

print(carJSON)
