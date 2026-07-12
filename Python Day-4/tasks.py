#Abstraction
# from abc import ABC, abstractmethod
# class Student(ABC):
#      @abstractmethod
#      def data(self, name, age, marks):
#         pass
# class Students(Student):
#      def data(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Marks :", self.marks)
#         if self.marks >= 35:
#             print("Result : Pass")
#         else:
#             print("Result : Fail")
# students1 = Students()
# students1.data("Siri", 22, 35)

#Encapsulation 
# class Student:
#     def __init__(self, name, age, marks):
#         self.__name = name
#         self.__age = age
#         self.__marks = marks
#     def display(self):
#         print("Name :", self.__name)
#         print("Age :", self.__age)
#         print("Marks :", self.__marks)
#         if self.__marks >= 35:
#             print("Result : Pass")
#         else:
#             print("Result : Fail")
# student1 = Student("Siri", 22, 35)
# student1.display()

#Inheritance
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age   
        self.marks=marks 
    def display(self):
       print("Student Details")
       print ("Name:",self.name)
       print("Age:",self.age)   
       print("Marks:",self.marks)
class Result(Student):
    def __init__(self, name, age, marks,grade):
        super().__init__(name,age,marks)
        self.grade=grade
    def display1(self):
        super().display()
        print("Grade:",self.grade)
student = Result("Siri", 22, 35,"pass")
student.display1()

#polymorphism
# class Student:
#     def display(self):
#         print("Student Details")
# class Result(Student):
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#     def display(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Marks :", self.marks)
#         if self.marks >= 35:
#             print("Result : Pass")
#         else:
#             print("Result : Fail")
# student1 = Result("Siri", 22, 35)
# student1.display()
        

       