
def palidromm(a):
    try :
        if a == a[::-1]:
            print("palidrom")
        else :
            print("No")
    except:
        print("Ошибка")
a = input()
palidromm(a)