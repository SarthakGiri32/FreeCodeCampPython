class Animal:
    def speak(self):
        return 'Some generic sound'


class Cat(Animal):
    def speak(self):
        return 'A cat meow'


class Dog(Animal):
    def speak(self):
        return 'A dog barks woof woof'


class Monkey(Animal):
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'


animals = [Cat(), Dog(), Monkey(), Animal()]

for animal in animals:
   print(animal.speak())

# Output:
# A cat meow
# A dog barks woof woof
# A monkey ooh ooh aah aah ooh ooh aah aah
# Some generic sound
