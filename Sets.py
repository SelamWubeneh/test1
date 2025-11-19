
#python SETS operations
# sets starts with curly braces{ }. we  can also use brace (( )), square bracket([]) or curly brace ({ })
#sets are not  ordered, when we print the valuse the orders might be different
#we can add and remove values but they are unchangeable
# the collectection should be unique and can not be duplicates
#can be any data type.. number or string
#unordered,unchanged,unindexed


# we use add if we want to add a single value " orange"
# we use update if we want to add multiple  sets. e.g set 1, se2. 3.....
#UPDATE operation- any itrate item list, string, set, dictionary

#Remove operation

#if you use remove for an item that dont exist or has removed already, py will print an error 
# discard operation- py will still print, even though the item does not exist. It won't be an error like remove

#pop operation

# removes a random item from set

#clear operation
#del


#Activity 

# colors = {"Yellow", "Orange", "Black"}
# print(colors)
# colors.update({"purple", "green","white"})
# print(colors)
# colors.remove("Orange")
# print(colors)

#UNION
# SYNTAX:
#  SetA.union(setB, setC, setD....)

#intersection 
# valuses that can only found in all sets. 
# ctivity2
# setA = {"Yellow", "Orange", "Black"}
# setB = {"Black", "Blue", "Yellow"}
# union_set = setA.union(setB)
# print("union:", union_set)

# setA.intersection_update(setB)
# print("Intersection(updated setA):", setA)

# setA = {"Yellow", "Orange", "Black"}
# diff_set = setA.difference(setB)
# print("Difference ( A - B ):", diff_set)

#.intersection() 
# sample_set_A = {"Yellow", "Orange", "Black"}
# sample_set_B = {"Black","Blue","Yellow"}

# common = sample_set_A.intersection(sample_set_B)
# if common:
#     print("Common elements:", common)
# else:
#     print("No common elements.")

#2add only unique elements from setB that are not already in setA.
# .difference_update() or combine logic.

# sample_set_A.update(sample_set_B.difference(sample_set_A))
# print(sample_set_A)


#3Remove items from Set A that are not common to both Set A and Set B.
#This means keep only the intersection.

# sample_set_A.intersection_update(sample_set_B)
# print(sample_set_A)






