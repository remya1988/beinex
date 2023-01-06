n=int(input("Enter the integer"))
lmt=int(input("Enter the limit of array"))
lst1=[]
lst_rotate=[]
for i in range(lmt):
    lst1.append(input("Enter the elemnt : "))

for data in range(lmt-n,lmt):
    lst_rotate.append(lst1[data])
for data in range(0,lmt-n):
    lst_rotate.append(lst1[data])

print(lst_rotate)