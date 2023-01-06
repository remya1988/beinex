num=int(input("Enter a number : "))
bin=[]
i=0
while(num>0):
    dig = num%2
    bin.insert(i,dig)
    i+=1
    num=num//2
print(bin[::-1])