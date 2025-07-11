n = int(input())
fn = list(map(int, input().split()))
pn = [False for _ in range(n)]
g = 0
cur = 0

for cur in range(n):
    while not(pn[cur]):#fn[cur]尚未拜訪
        pn[cur] = True
        if pn[fn[cur]]:
            g += 1
            break
        cur = fn[cur]
    
print(g)