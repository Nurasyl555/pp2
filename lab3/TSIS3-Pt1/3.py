def farm():
    for x in range(35):
        for y in range(35):
            if (x + y == 35) and (2*x + 4*y == 94):
                print("chickens -", x)
                print("rabbits -", y) 
                break
farm()