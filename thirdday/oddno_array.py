lmt=int(input("Enter the limit of array"))
lst1=[]
for i in range(lmt):
    lst1.append(int(input("Enter the elemnt : ")))
for item in lst1:
    if(item%2!=0):
        print(item)