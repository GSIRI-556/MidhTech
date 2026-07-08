# Basic functions
# def mssg():
#    print("hello")
#    print("Good Morning")
# mssg()
# mssg()  

#Prime Number without return value 
# number = int(input("Enter a number: "))
# if number <= 1:
#     print(number, "is Not a Prime Number")
# else:
#     for i in range(2, number):
#         if number % i == 0:
#             print(number, "is Not a Prime Number")
#             break
#     else:
#         print(number, "is a Prime Number")

#Functions using parameters
# def student_details(name,course):
#     print("Name of Student",name)
#     print("Course of Student",course)
# student_details("siri","cse")
# student_details("kd","aiml")  

#functions with return value
# def add(a,b):
#     return a+b
# print("Addition:",add(5,6))
# def sub(a,b):
#     return a-b
# print("subtraction:",sub(10,5))
# def mul(a,b):
#     return a*b
# print("Multiplication:",mul(5,2))
# def div(a,b):
#     return a/b
# print("Division:",div(10,2))

#prime number with return value
# def is_prime(num):
#     if num <= 1:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True


# number = int(input("Enter a number: "))

# if is_prime(number):
#     print(number, "is a Prime Number")
# else:
#     print(number, "is Not a Prime Number")  

#Recursion Factorial
# n= int(input("enter a number:"))
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print("Factorial of 5:",factorial(n))

