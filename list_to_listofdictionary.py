value_list1=["Black", "Red", "Maroon", "Yellow"]
value_list2=["#000000", "#FF0000", "#800000", "#FFFF00"]
key_list=['color_name','color_code']
res=[]
for i in range(0,len(value_list2)):
    res.append({key_list[0]:value_list1[i],key_list[1]:value_list2[i]})
print(res)