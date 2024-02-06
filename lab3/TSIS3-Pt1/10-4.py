def histogram(list2):
    for i in range(len(list2)):
        print("*"*list2[i], end=" ")
list1 = list(map(int, input().split()))
histogram(list1)