lst = []
n = int(input("Enter size of list : "))
for x in range(n):
    x=int(input("Enter element of List :"))
    lst.append(x)
largest = lst[0]
smallest = lst[0]
for i in range(n):
    if lst[i]>largest:
        largest = lst[i]
    if lst[i]<smallest:
        smallest = lst[i]

print("Smallest number : ",smallest)
print("Largest number : ",largest)
