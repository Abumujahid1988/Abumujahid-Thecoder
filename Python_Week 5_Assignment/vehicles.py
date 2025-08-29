## Activity 2: **Polymorphism Challenge** using vehicles

# Base class
class Vehicle:
    def move(self):
        pass   # This will be overridden by subclasses

# Subclasses with different implementations
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🛥️ The boat is sailing on the water.")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 The bicycle is pedaling on the track.")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # Each vehicle calls its own move() implementation