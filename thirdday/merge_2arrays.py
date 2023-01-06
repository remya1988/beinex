lst1=[]
lst2=[]
lst3=[]
n1=int(input("Enter the first array limit : "))
n2=int(input("Enter the second array limit : "))

for i in range(n1):
    lst1.append(input("Enter element"))
for i in range(n2):
    lst2.append(input("Enter element"))
lst3=lst1+lst2
print(lst3)

