def unique_elements(list1):
    list2 = []
    for x in list1:
        if x in list2:
            continue
        else :
            list2.append(x)
    return list2
list1 = list(map(int, input().split()))
unique_list = unique_elements(list1)
print(unique_list)