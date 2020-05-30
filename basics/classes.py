# a class is like a blueprint for creating objects

# Create class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend Class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and my balance is {self.balance}'


# Init user object
brad = User('Brad Traversy', 'test@gmail.com', 30)
# Init a customer
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)

print(janet.greeting())

print(brad.age)
brad.has_birthday()
print(brad.greeting())
