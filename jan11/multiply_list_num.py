
import arith_functions
lmt = int(input("Enter the limit : "))
lst=[]
for i in range(lmt):
    lst.append(int(input("Enter the elements : ")))
prod = arith_functions.multiply_list_numbers(lst)
print("Product of list items : ",prod)