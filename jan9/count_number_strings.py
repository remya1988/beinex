words=['abc', 'xyz', 'aba', '1221','909']
cnt=0

for wd in words:
    if len(wd)>=2 :
        if wd[0]==wd[-1]:
            cnt+=1
print("Count of words with first and last character same : ",cnt)