#public
# class Employee:
#     def __init__(self):
#         self.salary=5000
#     def display(self):
#         print("salary inside method:",self.salary)    
# obj=Employee()
# obj.display()
# print("outside the class:",obj.salary)     

#protected
# class Employee:
#     def __init__(self):
#         self._salary=5000
#     def display(self):
#         print("Inside method:",self._salary)    
# obj=Employee()
# obj.display()  
# print("outside the class:",obj._salary) 

#private
class Employee:
    def __init__(self):
        self.__salary=5000
    def display(self):
        print("Inside method:",self.__salary) 
obj=Employee()
obj.display()