mylist = ["apple", "banana", "cherry", "apple", "cherry"] # List is changeable, allow duplicate value
numberlist = [1, 2, 3, 4, 5]
boollist = [True, False, True]
list1 = ["abc", 34, True, 40, "male"] # List can contain different data types
print(type(mylist))# Class list


thislist = list(("apple", "banana", "cherry", "melon", "good", "bad")) # List constructor
print(thislist[1]) # Index start from 0
print(thislist[-1]) # Negative indexing means start from the end
print(thislist[2:5]) # Range of indexes, 5 not included
print(thislist[2:]) # From index 2 to the end

if "apple" in thislist:
    print("Yes, 'apple' is in the list")