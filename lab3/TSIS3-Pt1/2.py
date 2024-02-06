def temperature(Fahrenheit):
    c =  (5 / 9) * (Fahrenheit - 32)
    return c
f = float(input())
centigrade = temperature(f)
print(centigrade)
