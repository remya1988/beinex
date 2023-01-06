lst=[]
str=input("Enter the string : ")

for ch in str:
    lst.append(ch)

ch_cnt={}
for ch in lst:
    if ch in ch_cnt:
        ch_cnt[ch]+=1
    else:
        ch_cnt[ch]=1
print(max(ch_cnt.items(),key=lambda item:item[1]))