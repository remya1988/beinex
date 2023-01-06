def add(n1,n2):
    if (n2 == 0):
        return n1
    return add(n1, n2 - 1) + 1

num1=int(input("Enter first number : "))
num2=int(input("ENter second number : "))
sum = add(num1,num2-1)+1

print("Sum of ",num1," and ",num2," is ",sum)
