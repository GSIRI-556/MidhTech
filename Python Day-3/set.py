# set ordered
numbers={1,2,3,4,5,6,7,8,9,11,12,10}
print("example",numbers)

# set duplicates
roll_no={23,34,45,43,56,67,45}
print("set doesnot contain:",roll_no)

# converting into set
courses=["html","css","jss"]
print("converting datatype",tuple(courses))

# add,remove,len
set1={10,20,30}
print("original set:",set1)
set1.add(40)
print("After Adding:",set1)
set1.remove(20)
print("After removing:",set1)
len(set1)
print("Total students:",set1)

# task on set methods
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# add()
set1.add(70)
print("\nAfter add(70):", set1)

# update()
set1.update([80, 90])
print("After update([80, 90]):", set1)

# remove()
set1.remove(20)
print("After remove(20):", set1)

# discard()
set1.discard(100)  # No error if element doesn't exist
print("After discard(100):", set1)

# pop()
removed = set1.pop()
print("Removed using pop():", removed)
print("Set after pop():", set1)

# copy()
copy_set = set1.copy()
print("Copied Set:", copy_set)

# union()
print("\nUnion:", set1.union(set2))

# intersection()
print("Intersection:", set1.intersection(set2))

# difference()
print("Difference (set1 - set2):", set1.difference(set2))

# symmetric_difference()
print("Symmetric Difference:", set1.symmetric_difference(set2))

# issubset()
small_set = {30, 40}
print("\nIs small_set subset of set2?", small_set.issubset(set2))

# issuperset()
print("Is set2 superset of small_set?", set2.issuperset(small_set))

# isdisjoint()
set3 = {100, 200}
print("Is set2 disjoint with set3?", set2.isdisjoint(set3))

# intersection_update()
temp1 = {1, 2, 3, 4}
temp2 = {3, 4, 5, 6}
temp1.intersection_update(temp2)
print("\nAfter intersection_update():", temp1)

# difference_update()
temp3 = {1, 2, 3, 4}
temp3.difference_update({2, 4})
print("After difference_update():", temp3)

# symmetric_difference_update()
temp4 = {1, 2, 3}
temp4.symmetric_difference_update({3, 4, 5})
print("After symmetric_difference_update():", temp4)

# clear()
copy_set.clear()
print("\nAfter clear():", copy_set)