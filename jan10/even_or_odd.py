num=input("Enter a number : ")

if num.isnumeric():
    num=int(num)
    if num%2==0:
        print("Given number is even...")
    else:
        print("Given number is odd....")
else:
    print("Enter only numbers ")