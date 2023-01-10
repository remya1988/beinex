rn1 =int(input("Enter the start limit : "))
st_no=rn1
rn2 =int(input("Enter the end limit : "))
sum=0
while(rn1<=rn2):
    print(rn1)
    if(rn1%2!=0):
        sum+=rn1
    rn1=rn1+1
print("Sum of odd numbers between ",st_no," and ",rn2," is ",sum)