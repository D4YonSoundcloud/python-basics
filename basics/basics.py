# this is  comment

'''
multi line comment 
'''

'''
variable rules
 - variable names are case sensitive (name and NAME)
 -must start with a letter or an underscore
 - can have numbers but can not start with one
'''
# no semicolons

x = 1  # int
y = 2.5  # float
name = 'd4y'  # str
is_cool = True  # bool (must be capital T or F)

# multiple assignment

x, y, name, is_cool = (1, 2.5, 'd4y', True)

print('hello')

a = x + y

# casting

x = str(x)
y = int(y)
z = float(y)

print(x, y, name, is_cool, a)
print(type(z), z)

