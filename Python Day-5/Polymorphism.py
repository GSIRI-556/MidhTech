#overriding
# Child class changes parent's method
# class Payment:
#     def pay(self, amount):
#         print(f"Processing payment of ₹{amount}")
# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Credit Card")
# class UPI(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI")
# class NetBanking(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Net Banking")     
# credit = CreditCard()
# upi = UPI()
# bank = NetBanking()
# credit.pay(5000)
# upi.pay(2000)
# bank.pay(10000)           

#overloading
# Same method handles different arguments
class Salary:
    def calculate(self, basic, bonus=0, incentive=0):
        total = basic + bonus + incentive
        print("Salary =", total)
emp = Salary()
emp.calculate(30000)
emp.calculate(30000, 5000)
emp.calculate(30000, 5000, 2000)        