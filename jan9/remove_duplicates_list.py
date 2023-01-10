lmt=int(input("Enter the limit : "))
lst=[]
last_list=[]
for i in range(lmt):
    lst.append(input("Enter the elemt : "))

for num in lst:
    if num not in last_list:
        last_list.append(num)
print("Duplicates removed list is : ",last_list)
