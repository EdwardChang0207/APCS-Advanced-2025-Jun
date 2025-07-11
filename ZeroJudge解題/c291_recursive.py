n = int(input())
fn = list(map(int, input().split()))
pn = [False for _ in range(n)]
g = 0
cur = 0
def visit(cur, g):
    if not(pn[cur]):#fn[cur]尚未拜訪
        pn[cur] = True
        if pn[fn[cur]]:
            return g+1
        return visit(fn[cur], g)

    else:#fn[cur]已拜訪
        return g

for cur in range(n):
    g = visit(cur, g)
print(g)