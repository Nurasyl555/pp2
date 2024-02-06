def three(list2):
    for i in range(len(list2)-1):
        if list2[i] == 3 and list2[i+1] == 3:
            return True
    return False
numbers = list(map(int, input().split()))
has_3 = three(numbers)
print(has_3)

