str=input("Enter the string : ")
# cap_str=''
# for i in range(len(str)):
#     if i==0 or i== len(str):
#         str[i].upper()
#         print(str[i])
#     cap_str+=str[i]
# print(cap_str)
a = str.split()
res = []
for i in a:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)