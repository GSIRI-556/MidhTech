#single Inheritance
class Employee:
   def login(self):
        print("Employee logged in")
class Developer(Employee):
   def write_code(self):
        print("Writing Python code")
dev = Developer()
dev.login()
dev.write_code()

#Multiple Inheritance
class Payroll:
    def salary(self):
        print("Salary Processed")
class Attendance:
    def mark_attendance(self):
        print("Attendance Marked")
class Employee(Payroll, Attendance):
    def profile(self):
        print("Employee Profile")
emp = Employee()
emp.salary()
emp.mark_attendance()
emp.profile()

#MultiLevel Inheritance
class Bank:
    def open_account(self):
        print("Account Opened")
class SavingsAccount(Bank):
    def deposit(self):
        print("Money Deposited")
class PremiumSavings(SavingsAccount):
    def cashback(self):
        print("Cashback Credited")
customer = PremiumSavings()
customer.open_account()
customer.deposit()
customer.cashback()

#Hierarchical Inheritance
class Product:
    def show_price(self):
        print("Displaying Product Price")
class Mobile(Product):
    def brand(self):
        print("Samsung")
class Laptop(Product):
    def processor(self):
        print("Intel i7")
mobile = Mobile()
laptop = Laptop()
mobile.show_price()
mobile.brand()
laptop.show_price()
laptop.processor()

#Hybrid Inheritance
class Person:
    def details(self):
        print("Person Details")
class Doctor(Person):
    def diagnose(self):
        print("Diagnosing Patient")
class Research:
    def research(self):
        print("Medical Research")
class Surgeon(Doctor, Research):
    def surgery(self):
        print("Performing Surgery")
obj = Surgeon()
obj.details()
obj.diagnose()
obj.research()
obj.surgery()