lst1=[10, 15, 20, 25, 30, 35, 40]
lst2=[25, 40, 35]
lst3=[]
for item in lst1:
    if item not in lst2:
        lst3.append(item)

print("The difference is : ",lst3)