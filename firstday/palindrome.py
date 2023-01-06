num = int(input("Enter a number : "))
temp =num
rev =0

while(temp>0):
    dig = temp%10
    rev =rev*10+dig
    temp=temp//10

if(rev==num):
    print("The given number is Palindrome")
else:
    print("The given number is a not Palindrome")
