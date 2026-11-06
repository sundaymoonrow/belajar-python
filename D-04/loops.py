thislist = ["apple", "banana", "cherry", "melon", "kiwi", "watermelon"] # List constructor
# for x in thislist:
#     print(x)

# for i in range(len(thislist)):
#     print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

[print(x) for x in thislist]