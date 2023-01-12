import arith_functions
lmt = int(input("Enter the limit : "))
sample_list=[]
for i in range(lmt):
    sample_list.append(int(input("Enter the elements : ")))
unlst=arith_functions.make_uniquelist(sample_list)
print(unlst)
