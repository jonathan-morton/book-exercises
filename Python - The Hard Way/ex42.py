## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        #Dog has a name
        self.name = name

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## Mary's pet is satan
mary.pet = satan

## Frank is an Employee
frank = Employee("Frank", 120000)

## frank's pet is a rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()