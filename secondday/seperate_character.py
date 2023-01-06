str=input("Enter the string : ")
lst=[]
for ch in str:
    lst.append((ch))
print("Characters in string are ")
for i in range(0,len(str)):
    print(lst[i])