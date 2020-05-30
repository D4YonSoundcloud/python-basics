# a Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members

# Creat tuple
fruits = ('apples', 'oranges', 'Grapes')
# fruits2 = tuple(('apples', 'oranges', 'Grapes'))

# one value make sure to add trailing comma
# or it will be a str
fruits2 = ('Apples',)
print(fruits2, type(fruits2))

# get a value
print(fruits[1])

# cant change a value, causes error
# fruits[0] = 'Pears'

# delete a tuple
del fruits2

# get length
print(len(fruits))

# A set is acollection which is unordered and unindexed.
# No duplicate members

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# add duplicate
fruits_set.add('Apples')

print(fruits_set)

# clear set
fruits_set.clear()

print(fruits_set)

# delete
del fruits_set
