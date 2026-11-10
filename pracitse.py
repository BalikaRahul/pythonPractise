from abc import ABC, abstractmethod


# ============================================================
# 1. ABSTRACTION - Interface equivalent
# ============================================================

class Playable(ABC):
#you just define the method in the abstact class and your writing login in where you call the abstact class
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def fly(self): 
        pass


# ============================================================
# 1. ABSTRACTION - Abstract Class
# 3. ENCAPSULATION
# ============================================================

class Animal(ABC):

    # Constructor
    def __init__(self, name):
        # Encapsulation
        # __name is private (name-mangled)
        self.__name = name

    # Encapsulation - Getter
    def get_name(self):
        return self.__name

    # Abstract method
    @abstractmethod
    def make_sound(self):
        pass

    # Concrete method
    def sleep(self):
        print(self.__name + " is sleeping. Zzz...")


# ============================================================
# 2. INHERITANCE
# 4. POLYMORPHISM - Method Overriding
# ============================================================

class Dog(Animal, Playable):

    # Constructor
    def __init__(self, name):
        # Calls Animal constructor
        super().__init__(name)

    # Method Overriding
    def make_sound(self):
        print(self.get_name() + " says: Woof! Woof!")

    # Implementing Playable
    def play(self):
        print(self.get_name() + " is fetching a ball.")

    # Python doesn't support traditional method overloading.
    # We use a default parameter to achieve similar behavior.
    def play_with_toy(self, toy=None):

        if toy is None:
            self.play()
        else:
            print(self.get_name() + " is playing with a " + toy + ".")


# ============================================================
# 2. INHERITANCE
# 4. POLYMORPHISM - Method Overriding
# ============================================================

class Cat(Animal):

    # Constructor
    def __init__(self, name):
        super().__init__(name)

    # Method Overriding
    def make_sound(self):
        print(self.get_name() + " says: Meow!")


# ============================================================
# 5. COMPOSITION
# ============================================================

class PetOwner:

    def __init__(self, owner_name, pet):
        self.owner_name = owner_name
        self.pet = pet

    def call_pet(self):
        print(
            self.owner_name +
            " calls for " +
            self.pet.get_name() +
            "."
        )

        self.pet.make_sound()


# ============================================================
# 6. CLASSES AND OBJECTS
# ============================================================

# Creating objects

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")


# ============================================================
# 1. INHERITANCE & ENCAPSULATION
# ============================================================

print("--- Inheritance & Encapsulation ---")

# get_name() is inherited from Animal
print("My dog's name is:", my_dog.get_name())

# sleep() is inherited from Animal
my_dog.sleep()
my_cat.sleep()

print()


# ============================================================
# 2. POLYMORPHISM - METHOD OVERRIDING
# ============================================================

print("--- Polymorphism (Overriding) ---")

# Python list can contain different types of objects
my_pets = [my_dog, my_cat]

for pet in my_pets:
    # Python determines which make_sound()
    # implementation should be called.
    pet.make_sound()

print()


# ============================================================
# 3. POLYMORPHISM - OVERLOADING ALTERNATIVE
# ============================================================

print("--- Polymorphism (Overloading) ---")

# Calls play()
my_dog.play()

# Similar to Java's play("squeaky toy")
my_dog.play_with_toy("squeaky toy")

print()


# ============================================================
# 4. ABSTRACTION - INTERFACE EQUIVALENT
# ============================================================

print("--- Abstraction (Interface) ---")

# Playable reference equivalent
playable_pet = my_dog

playable_pet.play()

# playable_pet.make_sound() would work in Python because
# Python uses dynamic typing. This differs from Java's
# compile-time interface reference restriction.

print()


# ============================================================
# 5. COMPOSITION
# ============================================================

print("--- Composition ---")

# PetOwner HAS-A Cat
owner = PetOwner("Alice", my_cat)

owner.call_pet()