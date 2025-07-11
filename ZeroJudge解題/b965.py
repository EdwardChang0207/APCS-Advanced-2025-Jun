def F(matrix:list):
    matrix.reverse()
    return matrix

def T(matrix:list):
    old = matrix
    matrix = []
    for c in range(len(old[0])):
        row = []
        for r in range(len(old)):
            row.append(old[r][c])
        matrix.append(row)
    matrix = F(matrix)
    return matrix

R, C, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]
m = list(map(int, input().split()))
m.reverse()

for k in m:
    if k == 1:
        B = F(B)
    else:
        B = T(B)

print(len(B), len(B[0]))
for row in B:
    print(*row)#* -> for all