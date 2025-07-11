R,C,k,m = map(int, input().split())
game_map = [list(map(int,input().split())) for _ in range(R)]
delta = [[0 for _ in range(C)] for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(s:int, k=k):
    return -1*(s//k), s//k

def find_adj(delta:list, matrix:list, i:int, j:int):
    if matrix[i][j] == -1: return delta
    for k in range(4):
        x, y = dx[k], dy[k]
        if (i + x < 0) or (i + x >= len(matrix)): continue
        if (j + y < 0) or (j + y >= len(matrix[0])): continue
        if matrix[i+x][j+y] == -1: continue
        ds, dt = move(matrix[i][j])
        delta[i][j] += ds
        delta[i+x][j+y] += dt

    return delta

for _ in range(m):
    for i in range(R):
        for j in range(C):
            delta = find_adj(delta, game_map, i, j)
    for i in range(R):
        for j in range(C):
            game_map[i][j] += delta[i][j]
    delta = [[0 for _ in range(C)] for _ in range(R)]
    
game_map = [[i for i in row if i != -1] for row in game_map]

maximum = max([max(row) for row in game_map])
minimum = min([min(row) for row in game_map])
print(minimum)
print(maximum)