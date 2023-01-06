num = int(input("Enter the number :"))
sum = 0
temp=num
while(temp>0):
    d = temp%10
    sum += (d**3)
    temp=temp //10

if(num==sum):
    print("Number is amstrong number ")
else:
    print("Number is not an amstrong number")
