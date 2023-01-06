str=input("Enter the string : ")
lst=['a','A','e','E','i','I','o','O','u','U']
str1=""
for ch in str:
    if ch in lst:
        continue
    else:
        str1+=ch
print(str1)
