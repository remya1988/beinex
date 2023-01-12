def even_checking(*args):
    even_lst = []
    for i in range(len(args)):
        if (args[i] % 2 == 0):
            even_lst.append(args[i])
    return even_lst

def multiply_list_numbers(lst):
    prod =1
    for num in lst:
        prod*=num
    return prod


def find_largest(lst):
    l=0
    for i in range(len(lst)):
        if(lst[i]>l):
            l=lst[i]
    return l

def make_uniquelist(lst):
    unique_lst=[]
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst
