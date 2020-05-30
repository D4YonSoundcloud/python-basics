# A dictionary is a collection which is unordered
# changeable and indexed.
# no Duplicate members

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 47,
}

# constructor
# person2 = dict(first_name='Sara', last_name="Williams")

# get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/vale
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)
print(person)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'kevin', 'age': 29},
    {'name': 'Matt', 'age': 30},
]

print(people)
print(people[1]['name'])  # Kevin
