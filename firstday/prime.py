num = int(input("Enter a number : "))
f = 0
for i in range(2,num,1):
    if num%i == 0 :
        f = 1
        break
if f == 0 and num>1:
    print("The number ",num," is a prime number......")
else :
    print("The number ",num," is not a prime number.....")