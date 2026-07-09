student_record={"name":"siri","Id":59}
print(student_record)
#adding keyvalue pair
student_record["city"]="Hyderabad"
print("Adding element:",student_record)
#update the key value
student_record["name"]="G.Siri"
print("updating element:",student_record)

# Creating a Dictionary
student = {
    "id": 101,
    "name": "Siri",
    "course": "Python"
}

print("Original Dictionary:")
print(student)

# get()
print("\nUsing get():")
print(student.get("name"))

# keys()
print("\nDictionary Keys:")
print(student.keys())

# values()
print("\nDictionary Values:")
print(student.values())

# items()
print("\nDictionary Items:")
print(student.items())

# update()
student.update({"course": "Full Stack", "city": "Hyderabad"})
print("\nAfter update():")
print(student)

# copy()
student_copy = student.copy()
print("\nCopied Dictionary:")
print(student_copy)

# setdefault()
student.setdefault("age", 22)
print("\nAfter setdefault():")
print(student)

# pop()
student.pop("city")
print("\nAfter pop('city'):")
print(student)

# popitem()
student.popitem()
print("\nAfter popitem():")
print(student)

# fromkeys()
subjects = ["Python", "Java", "SQL"]
marks = dict.fromkeys(subjects, 0)
print("\nDictionary using fromkeys():")
print(marks)

# clear()
student_copy.clear()
print("\nAfter clear():")
print(student_copy)

# Using del
del student["course"]
print("\nAfter del:")
print(student)

# Adding a new key
student["city"] = "Hyderabad"
print("\nAfter Adding city:")
print(student)

# Updating a value
student["name"] = "G. Siri"
print("\nAfter Updating name:")
print(student)

# Checking key
print("\nChecking Key:")
print("id" in student)

