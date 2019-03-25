l= [1, [2, [3, [4]]]]
def nested_list(lst):
    n=0
    for i in lst:
        if isinstance(i, list):
            n+=nested_list(i)
        else:
            n+=i
    return n
print(nested_list(l))