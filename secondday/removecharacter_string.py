str=input("Enter the string : ")
ch_del =input("Enter the character to delete : ")
f=0
str1=''
for ch in str:
    if ch==ch_del:
        f = 1
        continue

    else:
        str1+=ch
if f==1:
    print(str1)
else:
    print("The character is not present in the string")
