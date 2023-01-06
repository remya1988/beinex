str=input("Enter the string : ")
lst=[]
lst=str.split(" ")
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")