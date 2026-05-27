class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)

# attr_name = input('Enter the attribute you want to see: ')
# print(getattr(person, attr_name, 'Attribute not found'))

# Loop through all attributes (variables) of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe
