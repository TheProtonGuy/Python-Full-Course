class Animal:

    species = 'test'

    def make_sound(self):
        print("Some generic sound")

    def eat(self):
        print("Eating some generic food")

class Dog(Animal):
    
    def make_sound(self):
        print("Bark! Bark! Bark!")

class GermanShepard(Dog):

    def eat(self):
        print("German shepard eating meat")

class Cat(Animal):

    def make_sound(self):
        print("Meow! Meow! Meow!")

dog = Dog()
print(dog.species)
dog.make_sound()

cat = Cat()
cat.make_sound()

german_shepard_dog = GermanShepard()
german_shepard_dog.eat()
german_shepard_dog.make_sound()