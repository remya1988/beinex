# def reverseList(lst, start, end):
#   while start <= end:
#     lst[start], lst[end] = lst[end], lst[start]
#     start += 1
#     end -= 1
#   print(lst)
# # Driver function to test above function
# lst=[]
# lmt=int(input("Enter the limit : "))
# for i in range(lmt):
#     el = input("Enter element : ")
#     lst.append(el)
# reverseList(lst, 0, lmt)
lst=[]
rev_lst=[]
lmt=int(input("Enter the limit : "))
for i in range(lmt):
     el = input("Enter element : ")
     lst.append(el)

print("Original array: ");
for i in range(0, len(lst)):
    print(lst[i]),
print("Array in reverse order: ");
#Loop through the array in reverse order
for i in range(len(lst)-1, -1, -1):
    rev_lst.append(lst[i])
print(rev_lst)

# Driver function to test above function

