#class and objects self keyword
# class student:
#     def display(self,name):
#         print("student name:",name)
# s1 = student()        
# s2 = student()
# s1.display("Siri")
# s2.display("Lasya")

#constructor used by  _init_()
#it runs automatically when object is created
#used to intialize the object data
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name",self.name)
#         print("Age",self.age) 
# s1=student("siri",21)
# s1.display()
# s2=student("Iris",22)
# s2.display()
# s3=student("kd",22)          
# s3.display()

#Encapsulation task
#public- name   accessible from anywhere
#protected - _name  accessible within the class and derived classes (by convention)
#private -__name   accessible within the class (name managing)


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#     def show_balance(self):
#         print("owner:",self.owner)
#         print("Balance:",self.__balance)
# account1=BankAccount("Siri",5000) 
# account1.show_balance()

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._account_type = "savings"
#         self.__balance= balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance +=amount
#     def withdraw(self,amount):
#         if 0<amount<= self.__balance:
#             self.__balance-= amount
#             print("withdrawal successful")
#         else:
#             print("Insufficient Balance or Invalid amount")
#     def show_balance(self):
#         print("Balance:",self.__balance)
# account = BankAccount("John",1000)
# print("owner:",account.owner)
# print("Account type:",account._account_type)
# account.deposit(500)
# account.withdraw(300)
# account.show_balance() 

# #inheritance
# class Animal:
#     def eat(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# dog1 =Dog()
# dog1.eat()
# dog1.bark() 


# class Animal:
#     def eat(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")
# class Cat(Animal):
#     def meow(self):
#         print("cat meows")
# class Lion(Animal):
#     def Roars(self):
#         print("Lion sounds")
# class Monkey(Animal):
#     def cracks(self):
#         print("Monkey cracks")  
# Dog1=Dog()
# Dog1.bark()
# cat1=Cat()
# cat1.meow()
# Lion1=Lion()
# Lion1.Roars()
# Monkey1=Monkey()
# Monkey1.cracks()       

#polymorphism
# class Dog:
#     def sound(self):
#         print("Dog Barks")
# class cat:
#     def sound(self):
#         print("cat meows")
# dog1= Dog()
# dog1.sound()
# cat1 = cat()
# cat1.sound()      

#method Overriding 
#method Overloading  

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog animals")

class Cat(Animal):
    def sound(self):
        print("cat meows")

animals=[Animal(),Dog(),Cat()] # stores different object types in same list

for animal in animals:
    animal.sound()

def add(a,b=0,c=0):
    return a+b+c

print("add(5):",add(5))
print("add(5,10):",add(5,10))
print("add(5,10,15):",add(5,10,15))

#Abstraction
# by using abc module we can create ABC means Abstarct Base class
# abstract method is used to declare a method thathild classes must implement
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car starts with a key")
car1=car()
car1.start()
