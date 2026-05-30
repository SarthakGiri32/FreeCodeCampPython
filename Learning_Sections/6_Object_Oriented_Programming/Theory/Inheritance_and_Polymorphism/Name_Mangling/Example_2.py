class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)
example2 = Example(
    'I should not be accessed from outside the class',
    'But I can be accessed from outside the class with name mangling'
)

print(example1.__dict__['_Example__private']) # I cannot be accessed directly from outside the class
print(example2.__dict__['_Example__private']) # But I can be accessed from outside the class with name mangling
