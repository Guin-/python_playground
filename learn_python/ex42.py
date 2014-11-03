 # Exercise 42: Is-A, Has-A Objects and classes

 # Is-A is used when talking about objects and classes that are related by a class relationship 
 # ie (Fish and Salmon)
 # Has-A is used when objects and classes are related only because they reference each other
 # ie (Salmon and Gills)

## Animal is-a object
class Animal(object):
	pass

## Make a class Dog that is-a Animal
## Class Dog has-a init function that takes self and name parameters
## Init function 
class Dog(Animal):
	
	def __init__(self, name):
		# ?
		self.name = name # from self get the name attribute and set it to name

## Cat is-a Animal
class Cat(Animal): 
	def __init__(self, name):
		## ??
		self.name = name

## Person is-a object
class Person (object):
	def __init__(self, name):
		## Person has-a variable name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary):
		## ?? Magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## Mary has-a pet "satan"
mary.pet = satan

## frank is-a Employee 
## frank has-a salary 1200000
frank = Employee("Frank", 1200000)


## frank has-a pet, rover
frank.pet = rover

## Flipper is-a instance of a Fish
flipper = Fish()

## crouse is-a instance of a Salmon
crouse = Salmon()

## harry is-a instance of a Halibut
harry = Halibut()



















