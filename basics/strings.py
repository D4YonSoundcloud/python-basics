name = 'brad'
age = 37

# concatenate
print('hello my name is ' + name + ' and i am ' + str(age))

# strint formatting

# arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# f-strings (only in python 3.6+)
print(f'hello my name is {name} and I am {age}')

# string methods

s = 'hello world'

# Capitalize string
print(s.capitalize(s))
# Make the whole string uppercase
print(s.upper(s))
# Make the whole string lowercase
print(s.lower(s))
# swaps characters in the string
print(s.swapcase())
# prints the length of the string
print(s.len(s))
# replaces the first argument with the second/
print(s.replace('world', 'everyone'))
# counts the number of instances
sub = 'h'
print(s.count(sub))
# starts with 
print(s.startswith('hello'))
#ends with
print(s.endswith('d'))
#split into a list
print(s.split())
# Find position
print(s.find('r'))
#is alphanumeric
print(s.isaslnum())
#is alphabetic
print(s.isalpha())
#is numeric
print(s.isnumeric())

