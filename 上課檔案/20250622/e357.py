def F(x):
    if x == 1: return 1
    if x % 2 == 0: return F(int(x/2))
    return F(x-1)+F(x+1)

print(F(6))
