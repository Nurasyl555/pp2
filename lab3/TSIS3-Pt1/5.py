from itertools import permutations
def all_permutation(list1):
    list2 = list(permutations(list1))
    return list2
list1 = list(map(int, input().split()))
list3 = all_permutation(list1)
print(*list3)