class Dog:
    def __init__(self, name):
        self._name = name
        self._paws = 4

    def speak(self):
        return "woof"

    def run(self):
        return "I am a running dog"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Chihuahua(Dog): # inheritance
    def speak(self):
        return "yap"

    def move(self):
        return super().run() # get instance of parent class

dog = Chihuahua("Carlos")
print(dog.name)
print(dog.speak())
print(dog.move())