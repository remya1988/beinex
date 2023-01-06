lst1 = []
f = 0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input(" ")
    lst1.append(ele)
print("List 1 : ", lst1)
lst2 = []
n1 = int(input("Enter number of elements to delete : "))
for i in range(0, n1):
    ele = input(" ")
    lst2.append(ele)
print("Items to remove : ", lst2)
for item1 in lst2:
    for item2 in lst1:
        if item1 == item2:
            lst1.remove(item1)
            f = 1

if f == 0:
    print("The elements not present in the list1")
else:
    print("Items removed list is ", lst1)
