lmt=int(input("Enter the limit of array"))
lst1=[]
sum=0
for i in range(lmt):
    lst1.append(int(input("Enter the elemnt : ")))
for item in lst1:
    sum+=item
print("Sum of array elements ",sum)