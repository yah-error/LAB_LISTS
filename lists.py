# LAB_LISTS

## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

### Q1: Write a Python program to sum all the items in the list.
### Q2: Write a Python program to get the largest number from the list.
### Q3: using List Comprehension , create a new list from the above list containing only even numbers.
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
Sum = sum(list)
print(Sum)
############################
############################
Max = max(list)
print(Max)
############################
new_list = [x for x in list if x % 2 == 0]
print(new_list)
############################
print(list[:5])



