n=int(input("Enter the number of lines : "))
for i in range(n):

    for j in range(0, i + 1):
        print("*", end="")
    print("\r")

for i in range(1, n):

    for j in range(i, n):
        print("*", end="")
    print()