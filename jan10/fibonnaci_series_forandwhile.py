lmt = int(input("Enter the limit : "))
n1=0
n2=1
next_num=0
fib_no=[n1,n2]

# Using for loop

# for i in range(2,lmt-2):
#     next_num = n1+n2
#     fib_no.append(next_num)
#     n1=n2
#     n2=next_num
# print("Fibonacci series : ",fib_no)

# Using while loop

i=3
while(i<=10):
   next_num=n1+n2
   fib_no.append(next_num)
   n1=n2
   n2=next_num
   i+=1

print("Fibonacci series ",fib_no)


