num=int(input("Enter a number : "))
oct=[]
i=0
while(num>0):
    dig = num%8
    oct.insert(i,dig)
    i+=1
    num=num//8
print(oct[::-1])
