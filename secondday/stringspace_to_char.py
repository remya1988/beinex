str=input("Enter the string : ")
ch_replace =input("Enter the character to delete : ")
str1=''
for ch in str:
    if ch==' ':
        ch=ch_replace
    str1+=ch
print(str1)

