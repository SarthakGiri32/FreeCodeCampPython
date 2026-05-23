my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False
print(my_set.isdisjoint(your_set)) # False
union_set = my_set | your_set
intersection_set = my_set & your_set
print(union_set)
print(intersection_set)
print(my_set - your_set)
print(my_set ^ your_set) # symmetric difference
my_set -= your_set
print(my_set)
