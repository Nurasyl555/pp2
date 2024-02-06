def spy_game(nums):
    a = 0
    b = 0
    c = 0
    for i in range(len(nums)):
        
        if nums[i] == 0 and a != 0:
            a = i

        elif nums[i] == 0 and a < i:
            b = i
        if nums[i] == 7:
            c = i
    if a < b < c:
        return True
    else :
        return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))