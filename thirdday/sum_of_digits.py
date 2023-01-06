

def sum_of_digits(n):
    if n==0:
        return 0
    return(n%10+sum_of_digits(int(n/10)))

num = int(input("Enter number : "))
sum = sum_of_digits(num)
print(sum)


