# Python program to display the Fibonacci sequence

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))


num = int(input("Enter the limit : "))

print("Fibonacci sequence:")
for i in range(num):
    print(fibonacci(i))
