def count_numbers(limit):
    number=1
    while number<=limit:
        yield number
        number +=1
for value in count_numbers(5):
    print(value)
