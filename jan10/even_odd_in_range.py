limit = int(input("Enter the limit : "))

even_lst=[]
odd_lst=[]
for i in range(2,limit,2):
    even_lst.append(i)
print("Even numbers are....")
print(even_lst)

for i in range(1,limit,2):
    odd_lst.append(i)
print("Odd numbers are....")
print(odd_lst)
