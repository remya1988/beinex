lst=[]
lmt=int(input("Enter the limit : "))
for i in range(lmt):
    lst.append(input("Enter item : "))
element=input("Enter the element : ")
if element in lst:
    print("Element present in list....")
else:
    print("Not in the list......")