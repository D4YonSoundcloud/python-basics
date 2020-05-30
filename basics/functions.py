
# create a function
# with a default argument
def sayHello(name='Sam'):

    print(f'Hello {name}')


sayHello()

# return values


def getSum(num1, num2):
    total = num1 + num2
    return total


num = getSum(3, 4)
print(num)


# A lamba function is a small anoynmous function
# A lamba function can take any num of args, but can
# only have one expression

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))
