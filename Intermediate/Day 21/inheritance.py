
# Class Inheritance
# In python a class chan inherit attributes as well as methods from another class.... it is called inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    # Animal is a class that we want to inherit from
    def __init__(self):
        super().__init__()
        # super refers to the parent class i.e. the Animal class. and
        # it initializes everything that the super class Animal has to the Fish class

    def swim(self):
        print("Moving in water...")

    def breathe(self):
        super().breathe()
        print("doing this underwater...")


nemo = Fish()
nemo.swim()
nemo.breathe()

