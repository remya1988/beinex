import arith_functions

lmt =int(input("Enter the limit : "))
lst=[]
for i in range(lmt):
    lst.append(int(input("Enter the numbers : ")))
l=arith_functions.find_largest(lst)
print("Largest number is ",l)