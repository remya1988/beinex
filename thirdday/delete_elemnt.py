lmt=int(input("Enter the limit of array : "))
lst1=[]
for i in range(lmt):
    lst1.append(int(input("Enter the element : ")))
ind = int(input("Enter the index of elemnet to delete : "))
lst1.remove(lst1[ind])
print(lst1)