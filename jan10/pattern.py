
lmt=int(input("Enter the limit : "))

# First pattern
print("***** First pattern *****")
k = lmt - 1
for i in range(0, lmt):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

# Second pattern
print("***** Second pattern *****")
for i in range(0, lmt):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

# Third pattern
print("***** Third pattern *****")
for i in range(0, lmt):
    for j in range(0, i + 1):
        print(i, end=" ")
    print("\r")

# Fourth pattern
print("***** Fourth pattern *****")
k=0
for i in range(0, lmt):
    for j in range(0, i + 1):
        # printing stars
        print(k, end=" ")
        k+=1
    print("\r")
