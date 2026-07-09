double= lambda x:x*2
print("Basic example:",double(5))

marks=[75,78,90]
bonus_marks=list(map(lambda mark: mark + 5,marks))
print("Bonus marks",bonus_marks)

marks = [75, 45, 90, 30, 80]
passed_students = list(filter(lambda mark: mark >= 50, marks))
print("Passed students:", passed_students)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)