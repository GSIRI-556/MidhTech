try:
    student = {
        "name": "Siri",
        "age": 22
    }
    print(student["marks"])
except KeyError:
    print("Key not found.")
finally:
    print("Program Finished")