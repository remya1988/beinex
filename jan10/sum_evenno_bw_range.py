rn1 =int(input("Enter the start limit : "))
rn2 =int(input("Enter the end limit : "))
sum=0
for i in range(rn1,rn2+1):
    if(i%2==0):
        sum+=i
    else:
        continue
print("Sum of even numbers between ",rn1," and ",rn2," is ",sum)