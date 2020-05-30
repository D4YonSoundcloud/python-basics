# a list a collection which is ordered and changeable.
# allows deuplicate members.
# list are 0 based

# create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'Grapes', 'Pears']

# user a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from List
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
