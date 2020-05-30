# if/else conditions are used to decide to do something
# based on something being true or false

x = 2
y = 10

# Comparison Operators (==, !=, >, <, >=, <=)

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{y} is equal than {x}')
else:
    print(f'{y} is greater than {x}')

# nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not)

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
# not
if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership Operators (not, not in)
numbers = [1, 2, 3, 4, 5]

# in
if(x in numbers):
    print(x in numbers)

#  not in
z = 13
if(z not in numbers):
    print(z not in numbers)

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)
