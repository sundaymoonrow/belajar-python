thislist = ["orange", "apple", "banana", "cherry", "melon", "kiwi", "watermelon"] # List constructor
thislist.sort() # Sort the list ascending
thislist.sort(reverse=True) # Sort the list descending
numlist = [100, 50, 65, 82, 23]
numlist.sort() # Sort the list ascending
print(thislist)
print(numlist)

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc) # Sort the list based on how close the number is to
print(thislist)