class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.
